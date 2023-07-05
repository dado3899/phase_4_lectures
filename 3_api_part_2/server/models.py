# There are many ways we can add constraints!
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

class Student(db.Model, SerializerMixin):
    __tablename__ = 'students'
    serialize_rules =('-schedules.student',)
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    student_code = db.Column(db.Integer, unique = True)
    email = db.Column(db.String)
    emergency_email = db.Column(db.String)

    @validates('email','emergency_email')
    def checkEmail(self,key,value):
        if '@' in value:
            return value
        else:
            raise ValueError("Not valid email")

    @validates('student_code')
    def checkCode(self,key,value):
        if len(str(value)) == 6:
            return value
        else:
            raise ValueError("Not valid student code")

class Teacher(db.Model, SerializerMixin):
    __tablename__ = 'teachers'
    serialize_only = ('id','name')
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    specialty = db.Column(db.String)
    email = db.Column(db.String)
    @validates("specialty")
    def validateSpecialty(self,key,value):
        print("in Validates ",Student.query.all())
        return value

class Schedule(db.Model,SerializerMixin):
    __tablename__ = 'schedules'

    serialize_rules = ('-student.schedules','-teacher.schedules')
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    period = db.Column(db.Integer)

    student_id = db.Column(db.Integer,db.ForeignKey('students.id'))
    teacher_id = db.Column(db.Integer,db.ForeignKey('teachers.id'))

    student = db.relationship('Student', backref="schedules")
    teacher = db.relationship('Teacher', backref="schedules")
    