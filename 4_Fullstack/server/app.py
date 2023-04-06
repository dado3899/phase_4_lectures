# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db revision --autogenerate -m 'Create tables' 
# flask db upgrade 

# Standard imports/boilerplate setup
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from models import db,Student,Teacher,Schedule

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
# New addition to aid in cors errors
CORS(app)

@app.route("/home")
def home():
    return ""

class All_Student(Resource):
    def get(self):
        json_obj = { "Type" : "Get"}
        res = make_response(jsonify(json_obj),200)
        return res

    def post(self):
        json_obj = { "Type" : "Post"}
        res = make_response(jsonify(json_obj),200)
        return res
api.add_resource(All_Student, '/students')

class One_Student(Resource):
    def get(self,id):
        one_student = Student.query.filter(Student.id == id).first()
        res = make_response(jsonify(one_student.to_dict()),200)
        return res
    def patch(self,id):
        one_student = Student.query.filter(Student.id == id).first()
        for attr in request.form:
            setattr(one_student, attr, request.form.get(attr))
        db.session.add(one_student)
        db.session.commit()
        res = make_response(jsonify(one_student.to_dict()),200)
        return res

    def delete(self,id):
        one_student = Student.query.filter(Student.id == id).first()
        db.session.delete(one_student)
        db.session.commit()
        res = make_response(jsonify(one_student.to_dict()),200)
        return res
api.add_resource(One_Student, '/students/<int:id>')

class All_Teacher(Resource):
    def get(self):
        all_students = Teacher.query.all()
        all_return = []
        for student in all_students:
            all_return.append(student.to_dict())
        res = make_response(jsonify(all_return),200)
        return res
api.add_resource(All_Teacher, '/teachers')

class All_Schedule(Resource):
    def get(self):
        all_schedule = Schedule.query.all()
        all_return = []
        for schedule in all_schedule:
            all_return.append(student.to_dict())
        res = make_response(jsonify(all_return),200)
        return res
api.add_resource(All_Schedule, '/schedules')

if __name__ == '__main__':
    app.run(port=5555)