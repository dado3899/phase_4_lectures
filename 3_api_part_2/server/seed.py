from app import app 
from models import db, Teacher, Student, Schedule
from faker import Faker
from random import randint
faker = Faker()
with app.app_context():
    print("Deleting Schedule")
    Schedule.query.delete()
    print("Deleting Teacher")
    Teacher.query.delete()
    print("Deleting Student")
    Student.query.delete()
    print("Seeding Students")
    students = []
    for i in range(50):
        sc = randint(1,999999)
        new_student = Student(name=faker.name(),gpa = 0,student_code=sc)
        students.append(new_student)
    db.session.add_all(students)

    print("Seeding Teachers")
    teachers = []
    for i in range(50):
        new_teacher = Teacher(name=faker.name(), email=faker.email(),emergency_email = faker.email())
        teachers.append(new_teacher)
    db.session.add_all(teachers)

    print("Seeding Schedule")
    schedules = []
    all_subjects = ['Math','Science','English','Spanish','Music','Art','CS']
    for i in range(50):
        for j in range(8):
            class_name = faker.word()+' 101'
            rand_int = randint(0,len(all_subjects)-1)
            rand_teacher = randint(1,50)
            new_schedule = Schedule(
                name = class_name,
                subject = all_subjects[rand_int], 
                period = j+1,
                student_id = i+1,
                teacher_id = rand_teacher
                )
            schedules.append(new_schedule)
    db.session.add_all(schedules)
    db.session.commit()