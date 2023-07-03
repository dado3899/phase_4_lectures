# There are many ways we can add constraints!
# db.CheckConstraint
# nullable = False
# unique = True
# @validates('')

# imports
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_`%(constraint_name)s`",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
    })

db = SQLAlchemy(metadata=metadata)
# Lets do a many to many!
# Join_class = relationship('Join_class', backref='many2')
# many1_id = Column(Integer, ForeignKey('many1_tablename.id'))
# many1_id = Column(Integer, ForeignKey('many2_tablename.id'))
# Join_class = relationship('Join_class', backref='many1')

class Teacher(db.Model,SerializerMixin):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String)
    emergency_email = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    schedules = db.relationship('Schedule', backref='teacher')
    students = association_proxy('schedules','student')

    serialize_rules = ('-schedules.teacher',)

    @validates('email','emergency_email')
    def check_email(self,key,value):
        if "@" in value:
            return value
        else:
            raise Exception("Invalid email")

class Student(db.Model,SerializerMixin):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable = False)
    gpa = db.Column(db.Float)
    student_code = db.Column(db.Integer,nullable = False, unique = True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    schedules = db.relationship('Schedule', backref='student')
    teachers = association_proxy('schedules','teacher')

    serialize_rules = ('-schedules.student',)

    @validates('student_code')
    def check_student_code(self,key,value):
        print(self.gpa)
        print(type(value))
        if 0 < int(value) < 1000000:
            return value
        else:
            raise Exception("Invalid student id")


class Schedule(db.Model,SerializerMixin):
    __tablename__ = "schedules"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    subject = db.Column(db.String)
    period = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    serialize_rules = ('-student.schedules','-teacher.schedules')

