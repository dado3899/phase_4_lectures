from review import app 
from models import *
import datetime

with app.app_context():
    # DELETE CURRETN TABLE INFO
    Order.query.delete()
    Customer.query.delete()
    Product.query.delete()
    print("Seeding customers")
    bob = Customer(
        name = "Bob",
        email = "Bob@gmail"
    )
    db.session.add(bob)
    db.session.commit()
    print("Seeding products")
    coke = Product(
        name = "12 pack of coke",
        company = "Coke Company"
    )
    db.session.add(coke)
    db.session.commit()
    print("seeding orders")
    o1 = Order(
        product = coke,
        customer = bob,
        price = 10.99,
        date = datetime.datetime.strptime("2024/04/25", '%Y/%m/%d').date()
    )
    db.session.add(o1)
    db.session.commit()