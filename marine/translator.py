__author__ = 'spousty aka TheSteve0'
import csv

infile_txt = '/home/spousty/data/MOLW/marine/859583.csv'
outfile = open('./all_obs.sql', 'w')


fields_in_order = ['identification', 'location', 'time_of_observation', 'sea_level_pressure', \
'characteristics_of_pressure_tendency', 'pressure_tendency', 'air_temperature', 'wet_bulb_temperature', \
'dew_point_temperature', 'sea_surface_temperature', 'wave_direction', 'wave_period', 'wave_height', 'swell_direction', \
'swell_period', 'swell_height', 'total_cloud_amount', 'low_cloud_amount', 'low_cloud_type', 'cloud_height_indicator', \
'cloud_height', 'middle_cloud_type', 'high_cloud_type', 'visibility', 'visibility_indicator', 'present_weather', \
'past_weather', 'wind_direction', 'wind_speed']

fields_to_quote = ['identification', 'time_of_observation', 'wave_direction', 'wave_period', 'swell_direction', \
'swell_period', 'low_cloud_type', 'cloud_height_indicator', 'cloud_height', 'middle_cloud_type', 'high_cloud_type',\
'visibility', 'visibility_indicator', 'present_weather', 'past_weather']

def make_first_sql(fields):
    sql_to_return = "INSERT INTO public.marineobs ("
    list_size = len(fields)
    for i in range(0, list_size):
        value = fields[i]

        # Don't append a , on the end of the last one
        if i != list_size-1:
            sql_to_return += value + ', '
        else:
            sql_to_return += value
    return sql_to_return + ') VALUES ('



def make_point(line):
    lat = line.pop('latitude')
    lon = line.pop('longitude')
    location_string = "ST_PointFromText('POINT("+ lon + " " + lat + ")', 4326)"
    line.update(location=location_string)

def make_timestamp(line):
    datetime = line['time_of_observation']
    datetime = datetime.replace("T", " ") + " -0"
    line.update(time_of_observation=datetime)

def quote_if_needed(value, field_name):
    if value == '' or value == 'X' or value == ' ':
        return "NULL"
    if field_name in fields_to_quote:
        return "'" + value + "'"
    else:
        return value


def make_sql_values(line, sql_to_build):
    list_size = len(fields_in_order)

    for i in range(0, list_size):
        field_value = line[fields_in_order[i]]

        # escape single quotes
        if "'" in field_value and fields_in_order[i] != "location":
            field_value = field_value.replace("'", "''")

        # Don't append a , on the end of the last one
        if i != list_size-1:
            sql_to_build += quote_if_needed(field_value, fields_in_order[i]) + ', '
        else:
            sql_to_build += quote_if_needed(field_value, fields_in_order[i])
    return sql_to_build + ');\n'

with open(infile_txt, 'r') as infile:
    reader = csv.DictReader(infile, delimiter=',')
    reader.fieldnames = [x.lower().replace(' ', '_').replace('/', '_') for x in reader.fieldnames]
    sql = make_first_sql(fields_in_order)

    outfile.write("BEGIN;")
    for line in reader:

        make_point(line)
        make_timestamp(line)
        final_sql = make_sql_values(line, sql)
        outfile.write(final_sql)
outfile.write("END TRANSACTION;")
print("Done")

infile.close()
outfile.close()