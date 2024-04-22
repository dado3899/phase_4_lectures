# Import SQLAlchemy from flask and from sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates

# This piece of code here is connected with the migrations:
# See here for more about this piece of code 
# https://docs.sqlalchemy.org/en/20/core/constraints.html#configuring-constraint-naming-conventions
metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
      })
# This will be our base, we can use our sqlalchemy method of making models using this!
db = SQLAlchemy(metadata=metadata)

# Lets create a class
class Yoyo(db.Model):
  __tablename__ = 'yoyos'

  id = db.Column(db.Integer, primary_key=True)
  rpm = db.Column(db.Integer)
  company = db.Column(db.String, nullable = False)
  size = db.Column(db.String)
  era = db.Column(db.Integer, nullable = False)

  @validates('era')
  def validate_era(self,key,value):
    print(value)
    valid_decades = (1970,1980,1990,2000,2010,2020)
    if value in valid_decades:
      return value
    else:
      raise ValueError("Not valid decade")