#Imports
from app import app 
# db and Production from models
from models import db, Student
from faker import Faker

# Create application context `with app.app_context():`
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/
with app.app_context():
# Using .query.delete() on the model will let us delete existing data
# Now we can start populating the data! 
    faker = Faker()
    print(faker.name())
    Student.query.delete()
    new_student = Student(name = "Ben", school = "Flatiron", student_code = 1)
    new_student2 = Student(name = "Cody", school = "Harvard && MIT", student_code = 2)
    code_start = 2
    db.session.add_all([new_student,new_student2])
    for i in range(5):
        code_start += 1
        new_student_faker = Student(name = faker.name(), school = "Flatiron", student_code = code_start)
        db.session.add(new_student_faker)
# We can no use the imported db to .add() and .commit()!
    db.session.commit()
    print(Student.query.all())