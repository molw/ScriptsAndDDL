import psycopg2
from geoalchemy2 import Geometry
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# taken from here http://docs.sqlalchemy.org/en/latest/orm/extensions/automap.html

Base = automap_base()

# engine
engine = create_engine("postgresql+psycopg2://spousty:notsafe@127.0.0.1/spousty")

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
Birdobs = Base.classes.birdobs

session = Session(engine)