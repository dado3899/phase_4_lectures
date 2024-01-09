from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData,ForeignKey
# This SerializerMixin import will allow us to call .to_dict()
# on data we query. If we add it to all connected tables
# we could see all the data turned to a dict
# We would need to add a line:
# serialize_rules = ('-tablename.value',)
# This will prevent a loop!
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# Reminder for foreign keys:
# In sqlalchemy we could have
# many = relationship('many_class', backref='one_tablename')
# one_id = Column(Integer, ForeignKey('one_tablename.id'))

# many1 = relationship('Join_class', backref='many2')
# many1_id = Column(Integer, ForeignKey('many1_tablename.id'))
# many1_id = Column(Integer, ForeignKey('many2_tablename.id'))
# many2 = relationship('Join_class', backref='many1')

class Teacher(db.Model,SerializerMixin):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    # Common additions to most tables to keep track of data! We don't need to add
    # anything when we are creating our seeds
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ('-students.teacher','-created_at','-updated_at')
    # serialize_only = ('id','name')

    students = db.relationship('Student',back_populates = "teacher")


class Student(db.Model,SerializerMixin):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    teacher_id = db.Column(db.Integer,db.ForeignKey('teachers.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    teacher = db.relationship('Teacher', back_populates = "students")

    serialize_rules = ('-teacher.students',)