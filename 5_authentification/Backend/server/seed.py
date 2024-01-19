from app import app 
from models import db, User
from faker import Faker
from random import randint
faker = Faker()
with app.app_context():
    print("Deleting Users")
    User.query.delete()
    new_user_1 = User(user_name="Cody", password_hash = "password")
    new_user_2 = User(user_name="Jack", password_hash = "password")
    new_user_3 = User(user_name="Emmi", password_hash = "password")
    users = [new_user_1,new_user_2,new_user_3]
    db.session.add_all(users)
    db.session.commit()