from review import Car, app, db

with app.app_context():
    car1 = Car(
        make = "Honda", 
        model = "Civic"
        )
    car2 = Car(
        make = "Chevy", 
        model = "Bolt"
        )
    # db.session.add(car1)
    # db.session.add(car2)
    db.session.add_all([car1,car2])
    db.session.commit()