from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates, relationship

# This SerializerMixin import will allow us to call .to_dict()
# on data we query. If we add it to all connected tables
# we could see all the data turned to a dict
# We would need to add a line:
# serialize_rules = ('-tablename.value',)
# This will prevent a loop!
metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
      })
db = SQLAlchemy(metadata=metadata)

class Teacher(db.Model, SerializerMixin):
    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    specialty = db.Column(db.String)
    lectures = relationship('Lecture', back_populates='teacher')
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ('-created_at','-updated_at','-lectures.teacher')
    # serialize_only = ('id','email')
    @validates('email')
    def validate_email(self,key,value):
        if "@" in value:
            return value
        else:
            raise ValueError("Not valid email")
        
class Lecture(db.Model, SerializerMixin):
    __tablename__ = "lectures"
    id = db.Column(db.Integer, primary_key = True)
    topic = db.Column(db.String)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    teacher = relationship('Teacher', back_populates='lectures')
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    student = relationship('Student', back_populates='lectures')

    serialize_rules = ('-created_at','-updated_at','-teacher.lectures','-student.lectures')

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

class Student(db.Model, SerializerMixin):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    grade = db.Column(db.Float)
    email = db.Column(db.String)

    lectures = relationship('Lecture', back_populates='student')

    serialize_rules = ('-created_at','-updated_at','-lectures.student')

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


# Reminder for foreign keys:
# In sqlalchemy we could have
# many = relationship('many_class', back_populates='one_tablename')
# one_id = Column(Integer, ForeignKey('one_tablename.id'))

# many1 = relationship('Join_class', backref='many2')
# many1_id = Column(Integer, ForeignKey('many1_tablename.id'))
# many1_id = Column(Integer, ForeignKey('many2_tablename.id'))
# many2 = relationship('Join_class', backref='many1')

class model():
    __tablename__ = ''
    id = db.Column(db.Integer, primary_key=True)

    # Common additions to most tables to keep track of data! We don't need to add
    # anything when we are creating our seeds
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Nice print'
