from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask.ext.sqlalchemy import SQLAlchemy
from app import app

engine = create_engine('postgres://trwloadfxdeybi:fusk2HrzpP6CUO_ha9N5olHlhg@ec2-54-225-168-181.compute-1.amazonaws.com:5432/d9mama8sl6rav4')
#engine = create_engine('postgresql+psycopg2://surajkapoor:wilshere10@localhost/lookbook')
app.config['SQLALCHEMY_DATABASE_URI'] = engine

Session = sessionmaker(bind=engine)
session = Session()

db = SQLAlchemy(app)