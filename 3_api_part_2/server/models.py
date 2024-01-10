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

metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
      })

db = SQLAlchemy(metadata=metadata)
# Lets do a many to many!
# many1 = relationship('Join_class', backref='many2')
# many1_id = Column(Integer, ForeignKey('many1_tablename.id'))
# many1_id = Column(Integer, ForeignKey('many2_tablename.id'))
# many2 = relationship('Join_class', backref='many1')

class Teacher(db.Model,SerializerMixin):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False,unique = True)
    email = db.Column(db.String, nullable = False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ('-schedules.teacher','-created_at','-updated_at')

    # students = db.relationship('Student',back_populates = "teacher")
    schedules = db.relationship('Schedule',back_populates = "teacher")

    @validates('email')
    def validate_email(self,key,value):
        if "@" in value:
            return value
        else:
            raise ValueError("Not valid email")

class Schedule(db.Model,SerializerMixin):
    __tablename__ = 'schedules'
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String)
    period = db.Column(db.Integer)
    teacher_id = db.Column(db.Integer,db.ForeignKey('teachers.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

    teacher = db.relationship('Teacher',back_populates = "schedules")
    student = db.relationship('Student',back_populates = "schedules")

    serialize_rules = ("-teacher.schedules","-student.schedules")

    

class Student(db.Model,SerializerMixin):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # teacher = db.relationship('Teacher', back_populates = "students")
    schedules = db.relationship('Schedule',back_populates = "student")
    serialize_rules = ('-schedules.student',)