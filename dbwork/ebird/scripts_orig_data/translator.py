__author__ = 'spousty aka TheSteve0'
import csv

infile_txt = '/home/spousty/data/MOLW/bird/BasicData/ebd_US-CA-087_prv_relNov-2016/ebd_US-CA-087_prv_relNov-2016.txt'
outfile = open('./all_obs.sql', 'w')

first_sql = '''INSERT INTO public.birdobs(global_unique_identifier, taxonomic_order, category,common_name, scientific_name,
subspecies_common_name, subspecies_scientific_name, observation_count, breeding_bird_atlas_code, age_sex, country,
country_code, state_province, subnational1_code, county, subnational2_code, iba_code, bcr_code, atlas_block, locality,
locality_id, locality_type, location, observation_start, observer_id, first_name, last_name, sampling_event_identifier,
protocol_type, project_code, duration_minutes, effort_distance_km, effort_area_ha, number_observers, all_species_reported,
group_identifier, approved, reviewed, reason, trip_comments, species_comments) VALUES ('''

def make_point(line):
    lat = line.pop('latitude')
    lon = line.pop('longitude')
    location_string = "ST_PointFromText('POINT("+ lon + " " + lat + ")', 4326)"
    line.update(location=location_string)

def make_timestamp(line):
    date = line.pop('observation_date')
    time = line.pop('time_observations_started')
    timestamp_string = date + " " + time
    line.update(observation_start=timestamp_string)

fields_in_order = ['global_unique_identifier','taxonomic_order','category', \
                   'common_name','scientific_name','subspecies_common_name','subspecies_scientific_name', \
                   'observation_count','breeding_bird_atlas_code','age_sex','country','country_code','state_province','subnational1_code', \
                   'county','subnational2_code','iba_code','bcr_code','atlas_block','locality','locality_id','locality_type', \
                   'location','observation_start','observer_id','first_name','last_name','sampling_event_identifier','protocol_type', \
                   'project_code','duration_minutes','effort_distance_km','effort_area_ha','number_observers','all_species_reported', \
                   'group_identifier','approved','reviewed','reason','trip_comments','species_comments']

fields_to_not_quote = ['taxonomic_order', 'observation_count', 'location', 'duration_minutes', 'effort_distance_km',\
                       'effort_area_ha', 'number_observers']


def quote_if_needed(value, field_name):
    if value == '' or value == 'X':
        return "NULL"
    if field_name in fields_to_not_quote:
        return value
    else:
        return "'" + value + "'"


def make_sql_values(line):
    sql = first_sql
    list_size = len(fields_in_order)

    for i in range(0, list_size):
        field_value = line[fields_in_order[i]]

        # escape single quotes
        if "'" in field_value and fields_in_order[i] != "location":
            field_value = field_value.replace("'", "''")

        # Don't append a , on the end of the last one
        if i != list_size-1:
            sql += quote_if_needed(field_value, fields_in_order[i]) + ', '
        else:
            sql += quote_if_needed(field_value, fields_in_order[i])
    return sql + ');'


with open(infile_txt, 'r') as infile:
    reader = csv.DictReader(infile, delimiter='\t')
    reader.fieldnames = [x.lower().replace(' ', '_').replace('/', '_') for x in reader.fieldnames]

    for line in reader:

        make_point(line)
        make_timestamp(line)
        final_sql = make_sql_values(line)

        outfile.write(final_sql)
print("Done")

infile.close()
outfile.close()