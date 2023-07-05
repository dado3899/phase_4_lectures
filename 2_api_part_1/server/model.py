from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
# This SerializerMixin import will allow us to call .to_dict()
# on data we query. If we add it to all connected tables
# we could see all the data turned to a dict
# We would need to add a line:
# serialize_rules = ('-tablename.value',)
# This will prevent a loop!
from sqlalchemy_serializer import SerializerMixin
# db = SQLAlchemy()

# Reminder for foreign keys:
# In sqlalchemy we could have
# many = relationship('many_class', backref='one_tablename')
# one_id = Column(Integer, ForeignKey('one_tablename.id'))

# many1 = relationship('Join_class', backref='many2')
# many1_id = Column(Integer, ForeignKey('many1_tablename.id'))
# many1_id = Column(Integer, ForeignKey('many2_tablename.id'))
# many2 = relationship('Join_class', backref='many1')

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
class Student(db.Model,SerializerMixin):
    __tablename__ = 'students'
    # serialize_only = ('id','name')
    # serialize_rules = ('-student_code',)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    student_code = db.Column(db.Integer)
    school = db.Column(db.String)
    schedules = db.relationship('Schedule', backref = 'student')

class Schedule(db.Model,SerializerMixin):
    __tablename__ = "schedules"
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    