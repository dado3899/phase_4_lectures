from app import app 
from models import db, Customer,Product,Order
from faker import Faker
from random import randint
faker = Faker()
with app.app_context():
    print("Deleting Customers")
    Customer.query.delete()
    print("Deleting Products")
    Product.query.delete()
    print("Deleting Orders")
    Order.query.delete()
    print("Seeding Customers")
    customers = []
    for i in range(50):
        new_cust = Customer(
            name=faker.name(),
            address = faker.address(),
            email = faker.email(),
            age = randint(1,100)
            )
        customers.append(new_cust)
    db.session.add_all(customers)

    print("Seeding Products")
    products = []
    for i in range(50):
        new_product = Product(
            name=faker.word(),
            description = faker.paragraph()
            )
        products.append(new_product)
    db.session.add_all(products)

    print("Seeding Orders")
    orders = []
    for i in range(50):
        new_order = Order(
            product_id = randint(1,50),
            customer_id = randint(1,50)
            )
        orders.append(new_order)
    db.session.add_all(orders)
    db.session.commit()

    new_cust_1 = Customer(
            name=faker.name(),
            address = faker.address(),
            email = faker.email(),
            age = randint(1,100)
        )
    new_product_1 = Product(
            name=faker.word(),
            description = faker.paragraph()
            )
    new_order = Order(
            product_id = new_product_1,
            customer_id = new_cust_1
            )
    db.session.add_all([new_cust_1,new_product_1,new_order])
    db.session.commit()