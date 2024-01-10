from app import app 
from models import db, Teacher,Student,Schedule
from faker import Faker
from random import randint
faker = Faker()

with app.app_context():
    Teacher.query.delete()
    Student.query.delete()
    for i in range(10):
        t = Teacher(
            name = faker.name(),
            email = faker.email()
        )
        db.session.add(t)
        db.session.commit()
    for i in range(10):
        s = Student(
            name = faker.name(),
            email = faker.email()
        )
        db.session.add(s)
        db.session.commit()
    for i in range(1,11):
        for j in range(1,9):
           sch = Schedule(
               class_name = "CS" + str(randint(100,500)),
               period = j,
               student_id = i,
               teacher_id = randint(1,11)
           )
           db.session.add(sch)
           db.session.commit()