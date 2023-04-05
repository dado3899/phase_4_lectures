# Set Up:
    # In Terminal, `cd` into `server` and run the following:
        # export FLASK_APP=app.py
        # export FLASK_RUN_PORT=5555
        # flask db init
        # flask db revision --autogenerate -m 'Create tables' 
        # flask db upgrade 
        # python seed.py

# | HTTP Verb 	|       Path       	| Description        	|
# |-----------	|:----------------:	|--------------------	|
# | GET       	|   /model       	| READ all resources 	|
# | GET       	| /model/:id    	| READ one resource   	|
# | POST      	|   /model      	| CREATE one resource 	|
# | PATCH/PUT 	| /model/:id    	| UPDATE one resource	|
# | DELETE    	| /model/:id    	| DESTROY one resource 	|

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
import json
from model import db, Vehicle, Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Note: `app.json.compact = False` configures JSON responses to print on indented lines
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
@app.route('/persons', methods = ['GET','POST'])
def get_people():
    if request.method == 'GET':
        all_peeps = Person.query.all()
        return_obj = []
        if all_peeps:
            for people in all_peeps:
                return_obj.append(people.to_dict())
            res = make_response(jsonify(return_obj),200)
            return res
        else:
            return_obj = {
                "valid": False,
                "Reason": "Can't query data"
            }
            res = make_response(return_obj,500)
            return res
    elif request.method == 'POST':
        newperson = Person(
            name = request.form.get("name"),
        )
        if newperson.name != None:
            db.session.add(newperson)
            db.session.commit()
            all_peeps = Person.query.all()
            new_peep = all_peeps[-1]
            res = make_response(jsonify(new_peep.to_dict()),201)
            return res
        else:
            return_obj = {
                "valid": False,
                "Reason": "Did not input name"
            }
            res = make_response(return_obj,500)
            return res

@app.route('/persons/<id>', methods = ['GET','PATCH','DELETE'])
def get_one_people(id):
    id_person = Person.query.filter(Person.id == id).first()
    if id_person:
        if request.method == 'GET':
            res = make_response(jsonify(id_person.to_dict()),200)
            return res
        elif request.method == 'PATCH':
            for attr in request.form:
               setattr(id_person, attr, request.form.get(attr))
            db.session.add(id_person)
            db.session.commit()
            res = make_response(jsonify(id_person.to_dict()),200)
            return res
        elif request.method == 'DELETE':
            db.session.delete(id_person)
            db.session.commit()
            return_obj = {
                "valid": True,
                "Reason": "Deleted"
            }
            res = make_response(return_obj,200)
            return res
    else:
        return_obj = {
            "valid": False,
            "Reason": "Not valid id"
        }
        res = make_response(return_obj,500)
        return res

@app.route('/vehicles/<id>', methods = ['GET','PATCH','DELETE'])
def get_one_vehicle(id):
    id_vehicle = Vehicle.query.filter(Vehicle.id == id).first()
    if id_vehicle:
        if request.method == 'GET':
            res = make_response(jsonify(id_vehicle.to_dict()),200)
            return res
        elif request.method == 'PATCH':
            for attr in request.form:
                if attr == 'registered':
                    setattr(id_vehicle, attr, bool(int(request.form.get(attr))))
                else:
                    setattr(id_vehicle, attr, request.form.get(attr))
            db.session.add(id_vehicle)
            db.session.commit()
            res = make_response(jsonify(id_vehicle.to_dict()),200)
            return res
        elif request.method == 'DELETE':
            db.session.delete(id_vehicle)
            db.session.commit()
            return_obj = {
                "valid": True,
                "Reason": "Deleted"
            }
            res = make_response(return_obj,500)
            return res
    else:
        return_obj = {
            "valid": False,
            "Reason": "Not valid id"
        }
        res = make_response(return_obj,500)
        return res

# Now thinking of paths we can add
# methods=['GET','POST'] to our @app.route('/anything')
# We can then check that request.method == 'GET' or 'POST' and do something accordingly
# For post we can go ahead and use request.form.get("field")
# EX newcar = Car(make = request.form.get("make"), model=request.form.get("model"))
# We would need to make sure our request has make and model! 
# response = make_response(newcar.to_dict(),201) as an example response
# 201 means a successful post!

# For patch we can use this:
# for attr in request.form:
#     setattr(queried_data, attr, request.form.get(attr))

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)