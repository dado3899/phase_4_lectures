# imports
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates,backref
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

#More boilerplate! Plys we need to import THE SAME bcrypt we created in app
# I would recommend moving that and db into a new file to avoid import errors
from sqlalchemy.ext.hybrid import hybrid_property
from services import bcrypt,db

class User(db.Model,SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique = True)
    user_type = db.Column(db.String)
    _password_hash = db.Column(db.String)
    # we need to create a _password_hash = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')
    def authenticate(self,password):
        return bcrypt.check_password_hash(self._password_hash,password.encode('utf-8'))

class Teacher(db.Model,SerializerMixin):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String)
    emergency_email = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    schedules = db.relationship('Schedule',cascade = "all,delete,delete-orphan",backref='teachers')
    serialize_rules = ('-schedules.teachers',)
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
    student_code = db.Column(db.Integer,nullable = False, unique = True)
    gpa = db.Column(db.Float)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # schedules = db.relationship('Schedule', backref='students')
    serialize_rules = ('-schedules.students',)

    @validates('student_code')
    def check_student_code(self,key,value):
        # print(type(value))
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
    students = db.relationship('Student', backref=backref('schedules', cascade = "all,delete,delete-orphan"))
    serialize_rules = ('-students.schedules','-teachers.schedules')

