# Import SQLAlchemy from flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# This will be our base, we can use our sqlalchemy method of making models using this!
metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
      })
db = SQLAlchemy(metadata=metadata)

# Lets create a class, first lets Pseudocode out the class
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    student_code = db.Column(db.Integer)
    school = db.Column(db.String)

class Schedule(db.Model):
    __tablename__ = "schedules"
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    