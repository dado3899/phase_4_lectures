# Import SQLAlchemy from flask
from flask_sqlalchemy import SQLAlchemy

# This will be our base, we can use our sqlalchemy method of making models using this!
db = SQLAlchemy()

# Lets create a class, first lets Pseudocode out the class
# vehicles
class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String)
    model = db.Column(db.String)
    year = db.Column(db.Integer)
    registred = db.Column(db.Boolean)

    def __repr__(self):
        return f'''
        Make: {self.make}
        Model: {self.model}
        Year: {self.year}
        '''


