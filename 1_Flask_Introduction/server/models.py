# Import SQLAlchemy from flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
      })
# This will be our base, we can use our sqlalchemy method of making models using this!
db = SQLAlchemy(metadata=metadata)

# Lets create a class, first lets Pseudocode out the class
# vehicles
class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String, unique = True)
    model = db.Column(db.String)
    year = db.Column(db.Integer)
    registered = db.Column(db.Boolean)

    def __repr__(self):
        return f'''
        Make: {self.make}
        Model: {self.model}
        Year: {self.year}
        '''


