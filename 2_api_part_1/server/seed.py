# Create seeds!
#Imports
from app import app
from model import db, Chef, Pastry

# Create application context `with app.app_context():`
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/

with app.app_context():
    print("Deleting....")
    Chef.query.delete()
    Pastry.query.delete()

    print("Making Chefs")
    nancy = Chef(
        name = "Nancy",
        specialty = "Croissant",
        phone = "111-111-1111"
    )
    ben = Chef(
        name = "Ben",
        specialty = "Pizza",
        phone = "222-222-2222"
    )
    db.session.add_all([nancy,ben])
    db.session.commit()

    print("Making Pastries")
    i1 = Pastry(
        name = "Croissant",
        country_of_origin = "France",
        moisture_content = 15,
        chef = nancy
    )
    i2 = Pastry(
        name= "Bear Claw",
        country_of_origin = "USA",
        moisture_content = 20,
        chef = nancy
    )
    i3 = Pastry(
        name = "Pizza (Cheese)",
        country_of_origin = "USA",
        moisture_content = 30,
        chef = ben
    )
    i4 = Pastry(
        name = "French Fries",
        country_of_origin = "Belgium",
        moisture_content = 10,
        chef = ben
    )
    db.session.add_all([i1,i2,i3,i4])
    db.session.commit()
