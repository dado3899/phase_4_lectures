#Imports
from app import app 
# db and Production from models
from models import db, Student,Teacher,Schedule
from faker import Faker

# Create application context `with app.app_context():`
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/
with app.app_context():
# Using .query.delete() on the model will let us delete existing data
# Now we can start populating the data! 
    faker = Faker()
    Student.query.delete()
    Teacher.query.delete()
    Schedule.query.delete()
    new_student = Student(name="Ben",student_code = 100001, email = "ben@email.com", emergency_email = "EMERGENCY@")
    new_student2 = Student(name="Cody",student_code = 100002, email = "cody@email.com", emergency_email = "EMERGENCY@")
    teacher = Teacher(name="David", email = "david@email.com", specialty = "Computer Science")
    schedule = Schedule(name = "Comp Sci 101", period = 1, student=new_student,teacher=teacher)
    schedule = Schedule(name = "Comp Sci 101", period = 1, student=new_student2,teacher=teacher)
    db.session.add_all([new_student,new_student2,teacher,schedule])
    db.session.commit()
    teacher2 = Teacher(name="Stephen", email = "stephen@email.com", specialty = "Computer Science")
    db.session.add(teacher2)
    db.session.commit()
    print(teacher.to_dict())
    print(schedule.to_dict())
    # Teacher.serialize_only = ('id','name','email')
    print(teacher.to_dict())
    # print(Student.query.all())