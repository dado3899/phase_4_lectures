from app import app 
from models import db, User
from faker import Faker
from random import randint
faker = Faker()
with app.app_context():
    print("Deleting Customers")
    User.query.delete()
    
    new_user_1 = User(username = "Zac")
    new_user_2 = User(username = "Jonathan")
    new_user_3 = User(username = "Jackson")
    users = [new_user_1,new_user_2,new_user_3]
    db.session.add_all(users)
    db.session.commit()