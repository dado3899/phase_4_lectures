# Import SQLAlchemy from flask
from flask_sqlalchemy import SQLAlchemy

# This will be our base, we can use our sqlalchemy method of making models using this!
db = SQLAlchemy()

# Lets create a class, first lets Pseudocode out the class
class NewClass(db.Model):
    __tablename__ = ''
    id = db.Column(db.Integer, primary_key=True)
