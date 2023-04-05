# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db revision --autogenerate -m 'Create tables' 
# flask db upgrade 
# Standard imports/boilerplate setup
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db,Student,Teacher,Schedule

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

# Differences between Flask Rest and Flask Restful?
# Restful setup
api = Api(app)
# @app.route('/vehicles/<id>', methods = ['GET','PATCH','DELETE'])
# def some_method():
#     if method == 'GET':
#         pass
#     elif method == 'PATCH':
#         pass

class All_Student(Resource):
    def get(self):
        all_students = Student.query.all()
        all_return = []
        for student in all_students:
            all_return.append(student.to_dict())
        res = make_response(jsonify(all_return),200)
        return res

    def post(self):
        new_student = Student(
            name =request.form.get("name"),
            student_code=request.form.get("student_code"),
            gpa=request.form.get("gpa")
        )
        db.session.add(new_student)
        db.session.commit()
        all_students = Student.query.all()
        ns = all_students[-1].to_dict()
        res = make_response(jsonify(ns),201)
        return res


    def print_hello(self):
        print("Hello")
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
# We can now use api.add_resource(class, '<path>')!
# But we need to create a class first and pass into it Resource
# We can now create a get post patch and delete!