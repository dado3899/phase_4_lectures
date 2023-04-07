from app import app 
from models import db, User
from faker import Faker
from random import randint
faker = Faker()
with app.app_context():
    print("Deleting Customers")
    User.query.delete()
    
    new_user_1 = User(name="Alex",user_type="Capricorn")
    new_user_2 = User(name="Jackie",user_type="Taurus")
    new_user_3 = User(name="Chris",user_type="Zebra")
    users = [new_user_1,new_user_2,new_user_3]
    db.session.add_all(users)
    db.session.commit()