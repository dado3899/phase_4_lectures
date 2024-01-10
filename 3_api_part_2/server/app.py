# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db revision --autogenerate -m 'Create tables' OR
# flask db migrate -m "Create Tables"
# flask db upgrade 
# Standard imports/boilerplate setup
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Teacher, Student,Schedule
from random import randint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

# Restful docs: https://flask-restful.readthedocs.io/en/latest/index.html
# Differences between Flask Rest and Flask Restful?
# What is a REST api? (representational state transfer)
# Restful setup
api = Api(app)

# @app.route('/teachers', methods = ["GET","POST"])
def teachers_route():
    all_teach = Teacher.query.all()
    if request.method == "GET":
        r_list = []
        for teach in all_teach:
            r_list.append(teach.to_dict(rules=('-students',)))
        print(r_list)
        return r_list, 200
    elif request.method == "POST":
        data = request.get_json()
        # print(data.get("NO","DEFAULT VALUE"))
        new_teach = Teacher(
            name = data.get("name","John Doe"),
            email = data.get("email")
        )
        db.session.add(new_teach)
        db.session.commit()
        return new_teach.to_dict(),200

class All_Teachers(Resource):
    def get(self):
        all_teach = Teacher.query.all()
        r_list = []
        for teach in all_teach:
            r_list.append(teach.to_dict(rules=('-students',)))
        print(r_list)
        return r_list, 200
    def post(self):
        data = request.get_json()
        # print(data.get("NO","DEFAULT VALUE"))
        new_teach = Teacher(
            name = data.get("name","John Doe"),
            email = data.get("email")
        )
        db.session.add(new_teach)
        db.session.commit()
        return new_teach.to_dict(),201

# @app.route("/random")
# def test():
#     rint = randint(0,1000)
#     return {"Test":rint},200
# @app.route('/teachers/<int:id>', methods = ["GET","PATCH","DELETE"])
def one_teacher_route(id):
    one_teach = Teacher.query.filter(Teacher.id == id).first()
    if not one_teach:
        return {"Error": "TEACHER DOES EXIST"},400
    if request.method == "GET":
        return one_teach.to_dict(), 200
    elif request.method == "PATCH":
        data = request.get_json()
        for attr in data:
            # Class object we are changing, variable name in obj, value we are changing to
            setattr(one_teach,attr,data.get(attr))
        db.session.add(one_teach)
        db.session.commit()
        return one_teach.to_dict(),200
    elif request.method == "DELETE":
        db.session.delete(one_teach)
        db.session.commit()
        return {"Status": "Deleted"},200

class One_Teacher(Resource):
    def get(self,id):
        one_teach = Teacher.query.filter(Teacher.id == id).first()
        return one_teach.to_dict(), 200
    def patch(self,id):
        one_teach = Teacher.query.filter(Teacher.id == id).first()
        data = request.get_json()
        for attr in data:
            # Class object we are changing, variable name in obj, value we are changing to
            setattr(one_teach,attr,data.get(attr))
        db.session.add(one_teach)
        db.session.commit()
        return one_teach.to_dict(),200
    def delete(self,id):
        one_teach = Teacher.query.filter(Teacher.id == id).first()
        db.session.delete(one_teach)
        db.session.commit()
        return {"Status": "Deleted"},200

class One_Schedule(Resource):
    def get(self,id):
        found_sched =Schedule.query.filter(Schedule.id==id).first()
        return found_sched.to_dict(),200

api.add_resource(All_Teachers, '/teachers')
api.add_resource(One_Teacher,'/teachers/<int:id>')
api.add_resource(One_Schedule,'/schedules/<int:id>')
# We can now use api.add_resource(class, '<path>')!
# But we need to create a class first and pass into it Resource

if __name__ == '__main__':
    app.run(port=5555, debug=True)