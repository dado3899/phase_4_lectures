from app import app 
from models import db, User
from faker import Faker
from random import randint
faker = Faker()
with app.app_context():
    print("Deleting Customers")
    User.query.delete()
    
    new_user_1 = User(name="Alex")
    new_user_2 = User(name="Jackie")
    new_user_3 = User(name="Chris")
    users = [new_user_1,new_user_2,new_user_3]
    db.session.add_all(users)
    db.session.commit()