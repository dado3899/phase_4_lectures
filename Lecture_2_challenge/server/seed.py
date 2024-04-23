from app import app
from model import db, Teacher, Lecture,Student
# Create seeds!

with app.app_context():
    Teacher.query.delete()
    Lecture.query.delete()
    Student.query.delete()

    t1 = Teacher(
        name = "David",
        email = "david.doan@flatironschool.com",
        specialty = "Python"
    )
    t2 = Teacher(
        name = "Stephen",
        email = "stephen.lambert@flatironschool.com",
        specialty = "Javascript"
    )
    s1 = Student(
        name = "Sam",
        grade = "4.0",
        email = "s@gmail.com"
    )
    s2 = Student(
        name = "Jonathan",
        grade = "3.9",
        email = "j@gmail.com"
    )

    db.session.add_all([t1,t2,s1,s2])
    db.session.commit()

    l1 = Lecture(
        topic = "Python basics",
        teacher = t1,
        student = s1
    )
    l6 = Lecture(
        topic = "Python basics",
        teacher = t1,
        student = s2
    )
    l2 = Lecture(
        topic = "Python orm",
        teacher = t1,
        student = s2
    )
    l3 = Lecture(
        topic = "Js basics",
        teacher = t2,
        student = s1
    )
    l5 = Lecture(
        topic = "Js basics",
        teacher = t2,
        student = s2
    )
    l4 = Lecture(
        topic = "CSS",
        teacher = t2,
        student = s1
    )
    db.session.add_all([l1,l2,l3,l4,l5,l6])
    db.session.commit()