#Imports
from app import app
from models import db, Computer

# Create application context `with app.app_context():`
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/

with app.app_context():
    Computer.query.delete()
    db.session.commit()
    c1 = Computer(
        brand = "Dell",
        memory = "1 million gigabytes",
        gpu = "Ryzen 960",
        ram = 700,
        laptop = True
    )
    c2 = Computer(
        brand = "Apple",
        memory = "03 gb",
        gpu = "2",
        ram = 1,
        laptop = True
    )
    db.session.add_all([c1,c2])
    db.session.commit()


# Using .query.delete() on the model will let us delete existing data
# Now we can start populating the data! 
# We can use the imported db to .add() and .commit()!