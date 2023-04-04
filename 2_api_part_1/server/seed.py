# Create seeds!

from app import app 
from model import db, Vehicle, Person
from faker import Faker
# Create application context `with app.app_context():`
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/
faker = Faker()
with app.app_context():
    print("Deleting Vehicles")
    Vehicle.query.delete()
    print("Deleting Persons")
    Person.query.delete()
    print("Seeding Persons")
    persons = []
    for i in range(5):
        fake_person = Person(name = faker.name())
        persons.append(fake_person)
    print("Seeding Vehicles")
    dodge_stratus =  Vehicle(make = "Dodge", model = "Stratus", year= 1, registered = False, person_id = 1)
    toyota_camery = Vehicle(make = "Toyota", model = "Camery", year= 1973, registered = True, person_id = 2)
    honda_civic = Vehicle(make = "Honda", model = "Civic", year= 2017, registered = False, person_id = 3)
    ferrari_laferrari = Vehicle(make = "Ferrari", model = "La Ferrari", year= 2000, registered = True, person_id = 3)
    all_vehicles = [dodge_stratus,toyota_camery,honda_civic,ferrari_laferrari]
    db.session.add_all(persons)
    db.session.add_all(all_vehicles)
    db.session.commit()

    # p1 = Person.query.filter(Person.id == 1).first()
    # print(p1.to_dict())