Create EXTENSION postgis;

DROP TABLE birdobs;

CREATE TABLE birdobs (

  global_unique_identifier VARCHAR(46) CONSTRAINT firstkey PRIMARY KEY,
  taxonomic_order FLOAT,
  category VARCHAR,
  common_name VARCHAR,
  scientific_name VARCHAR,
  subspecies_common_name VARCHAR,
  subspecies_scientific_name VARCHAR,
  observation_count SMALLINT,
  breeding_bird_atlas_code  VARCHAR,
  age_sex VARCHAR,
  country VARCHAR,
  country_code VARCHAR,
  state_province VARCHAR,
  subnational1_code VARCHAR,
  county VARCHAR,
  subnational2_code VARCHAR,
  iba_code VARCHAR,
  bcr_code VARCHAR,
  atlas_block VARCHAR,
  locality VARCHAR,
  locality_id VARCHAR,
  locality_type VARCHAR,
  location GEOMETRY(POINT,4326),
  observation_start TIMESTAMP,
  observer_id  VARCHAR,
  first_name VARCHAR,
  last_name VARCHAR,
  sampling_event_identifier VARCHAR,
  protocol_type VARCHAR,
  project_code VARCHAR,
  duration_minutes INT,
  effort_distance_km REAL,
  effort_area_ha REAL,
  number_observers INT,
  all_species_reported BOOLEAN,
  group_identifier VARCHAR,
  approved BOOLEAN,
  reviewed BOOLEAN,
  reason  VARCHAR,
  trip_comments VARCHAR,
  species_comments VARCHAR
);

CREATE INDEX birdobs_point_idx on birdobs USING GIST (location);