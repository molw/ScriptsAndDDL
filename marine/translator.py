__author__ = 'spousty aka TheSteve0'
import csv

infile_txt = './small_marine.csv'
outfile = open('./all_obs.sql', 'w')


fields_in_order = ['identification','time_of_observation', 'sea_level_pressure', \
'characteristics_of_pressure_tendency', 'pressure_tendency', 'air_temperature', 'wet_bulb_temperature', \
'dew_point_temperature', 'sea_surface_temperature', 'wave_direction', 'wave_period', 'wave_height', 'swell_direction', \
'swell_period', 'swell_height', 'total_cloud_amount', 'low_cloud_amount', 'low_cloud_type', 'cloud_height_indicator', \
'cloud_height', 'middle_cloud_type', 'high_cloud_type', 'visibility', 'visibility_indicator', 'present_weather', \
'past_weather', 'wind_direction', 'wind_speed']

def make_point(line):
    lat = line.pop('latitude')
    lon = line.pop('longitude')
    location_string = "ST_PointFromText('POINT("+ lon + " " + lat + ")', 4326)"
    line.update(location=location_string)

def make_timestamp(line):
    datetime = line['time_of_observation']
    datetime = datetime.replace("T", " ") + " -0"
    line.update(time_of_observation=datetime)

with open(infile_txt, 'r') as infile:
    reader = csv.DictReader(infile, delimiter=',')
    reader.fieldnames = [x.lower().replace(' ', '_').replace('/', '_') for x in reader.fieldnames]

    for line in reader:

        make_point(line)
        make_timestamp(line)

        # TODO need to make the SQL statement and then we are all done
#        final_sql = make_sql_values(line)

#        outfile.write(final_sql)
print("Done")

infile.close()
outfile.close()