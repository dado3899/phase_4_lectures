#Imports
# app from app
# db and Production from models

# Create application context `with app.app_context():`
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/
from app import app
from models import Pet, db

# Using .query.delete() on the model will let us delete existing data
with app.app_context():
    Pet.query.delete()
# Now we can start populating the data! 
# We can no use the imported db to .add() and .commit()!
    midna = Pet(
        name = "Midna",
        species = "Cat",
        age = 3
    )
    db.session.add(midna)
    db.session.commit()