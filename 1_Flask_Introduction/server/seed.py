#Imports
from app import app 
from models import db, Vehicle  

# Create application context `with app.app_context():`
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/

with app.app_context():
    print("Deleting data")
    Vehicle.query.delete()
    print("Seeding Vehicles")
    dodge_stratus =  Vehicle(make = "Dodge", model = "Stratus", year= 1, registred = False)
    toyota_camery = Vehicle(make = "Toyota", model = "Camery", year= 1973, registred = True)
    honda_civic = Vehicle(make = "Honda", model = "Civic", year= 2017, registred = False)
    ferrari_laferrari = Vehicle(make = "Ferrari", model = "La Ferrari", year= 2000, registred = True)
    all_vehicles = [dodge_stratus,toyota_camery,honda_civic,ferrari_laferrari]
    db.session.add_all(all_vehicles)
    db.session.commit()
# Using .query.delete() on the model will let us delete existing data
# Now we can start populating the data! 
# We can no use the imported db to .add() and .commit()!