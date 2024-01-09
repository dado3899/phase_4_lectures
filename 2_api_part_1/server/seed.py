# Create seeds!
from model import Teacher, db, Student
from app import app

with app.app_context():
    print("Deleting tables")
    Teacher.query.delete()
    Student.query.delete()

    print("Creating Teacher")
    t1 = Teacher(name = "David", email = "d@flatironschool.com")
    t2 = Teacher(name = "Stephen", email = "s@flatironschool.com")
    db.session.add_all([t1,t2])
    db.session.commit()

    print("Creating Student")
    s1 = Student(name = "Emmi", email = "e@flatironschool.com", teacher_id=t1.id)
    s2 = Student(name = "Dom", email = "dom@flatironschool.com", teacher_id=t1.id)
    s3 = Student(name = "Barret", email = "b@flatironschool.com", teacher_id=t2.id)
    db.session.add_all([s1,s2,s3])
    db.session.commit()


