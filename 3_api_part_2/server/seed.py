from faker import Faker
import random
from app import app
from models import *
import datetime

faker = Faker()

with app.app_context():
    Treaty.query.delete()
    Alliance.query.delete()
    Country.query.delete()

    for i in range(20):
        db.session.add(Country(
            name = faker.country()
        ))
    db.session.commit()

    for i in range(20):
        dt = datetime.datetime.strptime(faker.date(), '%Y-%m-%d')
        db.session.add(Alliance(
            name = faker.word(),
            date = dt.date()
        ))
    db.session.commit()
    for i in range(1,21):
        for j in range(3):
            db.session.add(Treaty(
                country_id = random.randint(1,20),
                alliance_id = i
            ))
    db.session.commit()