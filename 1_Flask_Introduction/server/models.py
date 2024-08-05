# Import SQLAlchemy from flask and from sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

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

# Lets create a classs
class Computer(db.Model):
    __tablename__ = 'computers'
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    memory = db.Column(db.String)
    gpu = db.Column(db.String)
    ram = db.Column(db.Integer)
    laptop = db.Column(db.Boolean)
    aesthetics = db.Column(db.Integer)
