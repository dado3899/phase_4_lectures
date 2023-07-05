# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db revision --autogenerate -m 'Create tables' 
# flask db upgrade 
# Standard imports/boilerplate setup
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db,Student
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

# Differences between Flask Rest and Flask Restful?
# Restful setup
api = Api(app)
CORS(app)

@app.route('/hello', methods=['GET','POST'])
def hello():
    method = request.method
    if method == "GET":
        return {"Hello":True}
    elif method == "POST":
        return {"Hello":False}

class allStudents(Resource):
    def get(self):
        all_students = Student.query.all()
        students_dict = []
        for student in all_students:
            students_dict.append(student.to_dict())
        return make_response(students_dict,200)
    def post(self):
        try:
            values = request.get_json()
            new_student = Student(
                name=values["name"],
                student_code = values["student_code"],
                email = values["email"],
                emergency_email = values["emergency_email"]
                )
            db.session.add(new_student)
            db.session.commit()
            return make_response(new_student.to_dict(),201)
        except:
            return make_response({"Failed": True}, 400)

class oneStudent(Resource):
    def patch(self,id):
        student = Student.query.filter(Student.id == id).first()
        values = request.get_json()
        for attr in values:
            setattr(student,attr,values[attr])
        db.session.add(student)
        db.session.commit()
        return make_response(student.to_dict(), 200)
    def delete(self,id):
        student = Student.query.filter(Student.id == id).first()
        db.session.delete(student)
        db.session.commit()
        return make_response({},200)

api.add_resource(allStudents,'/students')
api.add_resource(oneStudent,'/students/<id>')
# We can now use api.add_resource(class, '<path>')!
# But we need to create a class first and pass into it Resource