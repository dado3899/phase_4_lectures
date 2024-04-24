# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db revision --autogenerate -m 'Create tables' 
# flask db upgrade 
# Standard imports/boilerplate setup
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Country,Treaty,Alliance
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

@app.route('/countries', methods=['GET',"POST"])
def all_countries():
    if request.method == 'GET':
        ac = Country.query.all()
        return [country.to_dict() for country in ac]
    elif request.method == 'POST':
        try:
            data = request.get_json()
            c = Country(
                name = data['name'],
                capital = data.get('capital')
            )
            db.session.add(c)
            db.session.commit()
            return c.to_dict(),201
        except Exception as e:
            print(e)
            return {"Error": "Not valid data"}, 400
@app.route('/countries/<int:id>', methods=["GET","PATCH","DELETE"])
def one_county(id):
    found_country = Country.query.filter(Country.id == id).first()
    if found_country:
        if request.method == "GET":
            return found_country.to_dict()
        elif request.method == "PATCH":
            try:
                data = request.get_json()
                for key in data:
                    # setattr(What we are changing, the key we are changing, what we are changing it to)
                    setattr(found_country,key,data[key])
                db.session.add(found_country)
                db.session.commit()
                return found_country.to_dict(),202
            except Exception as e:
                print(e)
                return {"Error": "Cannot patch"},400
        elif request.method == "DELETE":
            at = Treaty.query.filter(Treaty.country_id==id).all()
            for treaty in at:
                db.session.delete(treaty)
            db.session.delete(found_country)
            db.session.commit()
            return {}, 204
    else:
        return {"Error": f"Country of id {id} doesn't exist"},400


# Differences between Flask Rest and Flask Restful?
# Restful setup
class all_alliance(Resource):
    def get(self):
        al = Alliance.query.all()
        return [alliance.to_dict() for alliance in al]
    def post(self):
        try:
            data = request.get_json()
            a = Alliance(
                name = data['name'],
                date = datetime.datetime.strptime(data['date'], '%Y-%m-%d').date()
            )
            db.session.add(a)
            db.session.commit()
            return a.to_dict(),201
        except Exception as e:
            print(e)
            return {"Error": "Not valid data"},400

class one_alliance(Resource):
    def get(self,id):
        found_alliance = Alliance.query.filter(Alliance.id == id).first()
        if found_alliance:
            return found_alliance.to_dict()
        else:
            return {"Error": f"Allance of id {id} does not exist"}
    def patch(self,id):
        found_alliance = Alliance.query.filter(Alliance.id == id).first()
        if found_alliance:
            try:
                data = request.get_json()
                for key in data:
                    if key == "date":
                        setattr(found_alliance, key, datetime.datetime.strptime(data[key], '%Y-%m-%d').date())
                    else:
                        setattr(found_alliance, key, data[key])
                db.session.add(found_alliance)
                db.session.commit()
                return found_alliance.to_dict(),202
            except Exception as e:
                print(e)
                return {'Error': "Cannot patch"},400
        else:
            return {"Error": f"Allance of id {id} does not exist"}
    def delete(self,id):
        found_alliance = Alliance.query.filter(Alliance.id == id).first()
        if found_alliance:
            db.session.delete(found_alliance)
            db.session.commit()
            return {},204
        else:
            return {"Error": f"Allance of id {id} does not exist"}
api.add_resource(all_alliance,'/alliances')
api.add_resource(one_alliance,'/alliances/<int:id>')
# But we need to create a class first and pass into it Resource
# We can now use api.add_resource(class, '<path>')!

if __name__ == '__main__':
    app.run(port=5555, debug=True)