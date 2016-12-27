__author__ = 'spousty aka TheSteve0'
import csv

infile_txt = './birdsample_larger.csv'
outfile = open('./birdsample_larger.ddl', 'w')

def make_point(line):
    lat = line.pop('LATITUDE')
    lon = line.pop('LONGITUDE')
    location_string = "ST_PointFromText('POINT("+ lon + " " + lat + ")', 4326)"
    line.update(location=location_string)

def make_timestamp(line):
    date = line.pop('OBSERVATION DATE')
    time = line.pop('TIME OBSERVATIONS STARTED')
    timestamp_string = date + " " + time
    line.update(observation_start=timestamp_string)



with open(infile_txt, 'r') as infile:
    reader = csv.DictReader(infile, delimiter='\t')

    first_sql = "INSERT INTO public.birdobs(global_unique_identifier, taxonomic_order, taxonomic_category,\
common_name, scientific_name, subspecies_common_name, subspecies_scientific_name,\
observation_count, breeding_bird_atlas_code, age_sex, country, country_code, state_province, subnational1_code,\
county, subnational2_code, iba_code, bcr_code, atlas_block, locality, locality_id, locality_type,\
location, observation_start, observer_id, first_name, last_name, sampling_event_identifier, protocol_type,\
project_code, duration_minutes, effort_distance_km, effort_area_ha, number_observers, all_species_reported,\
group_identifier, approved, reviewed, reason, trip_comments, species_comments) VALUES ("

    # TODO turn the keys into the column names
    # TODO Then make a list in the exact order of the columns names above
    # TODO then make a function which appends the names on to the SQL Statement one by one
    # TODO also handle the X in some columns for missing values
    # TODO also how to handle missing values in numeric columns- I think it is NaN
    for line in reader:

        make_point(line)
        make_timestamp(line)
        sql_string = first_sql + "'" + line['GLOBAL UNIQUE IDENTIFIER']+"'," +line['TAXONOMIC ORDER']
        sql_string += ');'
        # del line['LATITUDE']
        print(sql_string)

infile.close()
outfile.close()