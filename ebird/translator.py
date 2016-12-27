__author__ = 'spousty aka TheSteve0'
import csv

# work needs to be done on the coordinates and the date and time

infile_txt = './birdsample_larger.csv'


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

    for line in reader:

        make_point(line)
        make_timestamp(line)

        #del line['LATITUDE']
        print(line)