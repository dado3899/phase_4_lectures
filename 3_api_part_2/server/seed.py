# Create seeds!
#Imports
from app import app
from models import db, Chef, Pastry, Ingredient, Recipe
from faker import Faker
import random

# Create application context `with app.app_context():`
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/

with app.app_context():
    faker = Faker()
    print("Deleting....")
    Chef.query.delete()
    Pastry.query.delete()
    Ingredient.query.delete()

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
        moisture_content = 15
    )
    i2 = Pastry(
        name= "Bear Claw",
        country_of_origin = "USA",
        moisture_content = 20
    )
    i3 = Pastry(
        name = "Pizza (Cheese)",
        country_of_origin = "USA",
        moisture_content = 30
    )
    i4 = Pastry(
        name = "French Fries",
        country_of_origin = "Belgium",
        moisture_content = 10
    )
    db.session.add_all([i1,i2,i3,i4])
    db.session.commit()

    join1 = Recipe(
        chef_id = 1,
        pastry_id = 1
    )
    join2 = Recipe(
        chef_id = 2,
        pastry_id = 1
    )
    join3 = Recipe(
        chef_id = 1,
        pastry_id = 2
    )
    join4 = Recipe(
        chef_id = 2,
        pastry_id = 3
    )
    join5 = Recipe(
        chef_id = 2,
        pastry_id = 4
    )
    db.session.add_all([join1,join2,join3,join4,join5])
    db.session.commit()


    ing_list = []
    for i in [i1,i2,i3,i4]:
        ing = Ingredient(
            name= faker.word(),
            amount = random.randint(1,100),
            measurement_type = "Oz",
            pastry = i
        )
        ing2 = Ingredient(
            name= faker.word(),
            amount = random.randint(1,100),
            measurement_type = "Oz",
            pastry = i
        )
        ing_list.append(ing)
        ing_list.append(ing2)
    db.session.add_all(ing_list)
    db.session.commit()


