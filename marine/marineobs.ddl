CREATE EXTENSION postgis;

DROP TABLE marineobs;

CREATE TABLE marineobs (

marine_observation_id BIGSERIAL CONSTRAINT firstkey PRIMARY KEY,
identification VARCHAR,
location GEOMETRY(POINT,4326),
time_of_observation TIMESTAMPTZ,
sea_level_pressure FLOAT,
characteristics_of_pressure_tendency SMALLINT,
pressure_tendency FLOAT,
air_temperature FLOAT,
wet_bulb_temperature FLOAT,
dew_point_temperature FLOAT,
sea_surface_temperature FLOAT,
wave_direction VARCHAR,
wave_period VARCHAR,
wave_height FLOAT,
swell_direction VARCHAR,
swell_period VARCHAR,
swell_height FLOAT,
total_cloud_amount SMALLINT,
low_cloud_amount SMALLINT,
low_cloud_type VARCHAR,
cloud_height_indicator VARCHAR,
cloud_height VARCHAR,
middle_cloud_type VARCHAR,
high_cloud_type VARCHAR,
visibility VARCHAR,
visibility_indicator VARCHAR,
present_weather VARCHAR,
past_weather VARCHAR,
wind_direction INT,
wind_speed FLOAT

);

CREATE INDEX marineobs_point_idx on marineobs USING GIST (location);