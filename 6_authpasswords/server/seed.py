from app import app 
from models import db, User
from faker import Faker
from random import randint
faker = Faker()
with app.app_context():
    print("Deleting users")
    User.query.delete()

    u1 = User(
        username = "Jonathan",
        password_hash = "starlink"
    )
    u2 = User(
        username = "Zac",
        password_hash = "west"
    )
    u3 = User(
        username = "Sab",
        password_hash = "west"
    )
    db.session.add_all([u1,u2,u3])
    db.session.commit()