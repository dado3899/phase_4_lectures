# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db migrate -m 'Create tables' 
# flask db upgrade 
# Standard imports/boilerplate setup
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route("/pastries",methods=["GET","POST"])
def all_pastries():
    if request.method == "GET":
        ap = Pastry.query.all()
        return [pastry.to_dict() for pastry in ap]
    elif request.method == "POST":
        try:
            data = request.get_json()
            np = Pastry(
                name = data["name"],
                moisture_content = data["moisture"],
                country_of_origin = data["country"]
            )
            db.session.add(np)
            db.session.commit()
            return np.to_dict(),201
        except Exception as e:
            print(e)
            return {
                "Error": "Validation Error"
            },400


@app.route("/pastries/<int:id>",methods=["GET","PATCH","DELETE"])
def one_pastry(id):
    pastry = Pastry.query.filter(Pastry.id == id).first()
    if pastry:
        if request.method == "GET":
                return pastry.to_dict()
        elif request.method=="PATCH":
            try:
                data = request.get_json()
                for key in data:
                    # setattr(object you are changing, key you are changing, what you are changing it to)
                    setattr(pastry,key,data[key])
                db.session.add(pastry)
                db.session.commit()
                return pastry.to_dict(),200
            except Exception as e:
                print(e)
                return {
                    "error": "Validation Error"
                },400
        elif request.method=="DELETE":
            db.session.delete(pastry)
            db.session.commit()
            return {}
                
    else:
        return {
            "Error": "Not valid id"
        },400


# Differences between Flask Rest and Flask Restful?
# Representational State Transfer
# Rest: A architectural style of development that follows a specific set of rules (not all but has some)
# Restful: Follows most if not all of the rules and also tends to apply to webdev and resources
# SOAP?: Simple Object Access Protocol, very specific backend.

# Restful setup
api = Api(app)

class AllChef(Resource):
    def get(self):
        ac = Chef.query.all()
        return [chef.to_dict() for chef in ac]
    def post(self):
        try:
            data = request.get_json()
            c = Chef(
                name=data["name"],
                specialty=data.get("specialty"),
                phone=data["phone"]
            )
            db.session.add(c)
            db.session.commit()
            return c.to_dict()
        except Exception as e:
            print(e)
            return {
                "error": "Validation Error"
            },400

api.add_resource(AllChef,"/chefs")

class OneChef(Resource):
    def get(self,id):
        chef = Chef.query.filter(Chef.id == id).first()
        if chef:
            return chef.to_dict()
        else:
            return {
                "error": "not valid id"
            },400
    def patch(self,id):
        chef = Chef.query.filter(Chef.id == id).first()
        if chef:
            try:
                data = request.get_json()
                for key in data:
                    setattr(chef,key,data[key])
                db.session.add(chef)
                db.session.commit()
                return chef.to_dict()
            except Exception as e:
                print(e)
                return {
                    "error": "validation error"
                }
        else:
            return {
                "error": "not valid id"
            },400
    def delete(self,id):
        chef = Chef.query.filter(Chef.id == id).first()
        if chef:
            db.session.delete(chef)
            db.session.commit()
        else:
            return {
                "error": "not valid id"
            },400
# We can now use api.add_resource(class, '<path>')!
# But we need to create a class first and pass into it Resource

if __name__ == '__main__':
    app.run(port=5555, debug=True)