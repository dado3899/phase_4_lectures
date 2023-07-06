from app import app 
from models import db, User
from faker import Faker
from random import randint
faker = Faker()
with app.app_context():
    print("Deleting Customers")
    User.query.delete()
    
    new_user_1 = User(user="Ben", password_hash="benjam")
    new_user_2 = User(user="Cody", password_hash="24738291u481293")
    new_user_3 = User(user="Jacob",password_hash="p4ssw0rd")
    users = [new_user_1,new_user_2,new_user_3]
    db.session.add_all(users)
    db.session.commit()