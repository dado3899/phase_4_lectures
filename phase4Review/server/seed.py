from app import app 
from models import db, User,Schedule,Teacher,Student
from faker import Faker
from random import randint
faker = Faker()
with app.app_context():
    print("Deleting Customers")
    User.query.delete()
    print("Deleting Schedule")
    Schedule.query.delete()
    print("Deleting Teacher")
    Teacher.query.delete()
    print("Deleting Student")
    Student.query.delete()
    
    new_user_1 = User(name="Alex",user_type="Capricorn")
    new_user_2 = User(name="Jackie",user_type="Taurus")
    new_user_3 = User(name="Chris",user_type="Zebra")
    users = [new_user_1,new_user_2,new_user_3]
    db.session.add_all(users)
    db.session.commit()

    
    print("Seeding Students")
    students = []
    for i in range(50):
        sc = randint(1,999999)
        new_student = Student(name=faker.name(), student_code=sc,gpa = 0)
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


