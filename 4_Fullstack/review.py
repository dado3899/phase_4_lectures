# request.get_json() and data type talks
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db,Student,Teacher,Schedule
