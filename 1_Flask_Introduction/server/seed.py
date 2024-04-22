#Imports
# app from app
from app import app
# db and Production from models
from models import db, Yoyo

# Create application context `with app.app_context():`
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/
with app.app_context():
    Yoyo.query.delete()

    y1 = Yoyo(
        rpm = 100,
        company = "Yoyo Inc",
        size = 1,
        era = 1990
    )
    y2 = Yoyo(
        rpm = 50,
        company = "Yoyo Inc",
        size = 6,
        era = 1990
    )
    y3 = Yoyo(
        rpm = 2000,
        company = "Yoyo and company",
        size = 2,
        era = 1990
    )
    db.session.add_all([y1,y2,y3])
    db.session.commit()
# Using .query.delete() on the model will let us delete existing data
# Now we can start populating the data! 
# We can no use the imported db to .add() and .commit()!