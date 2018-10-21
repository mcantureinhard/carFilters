from flask import Blueprint
from flask import Response
from flask import request
from app import app
from json import dumps

rest_api = Blueprint('rest_api', __name__)

@rest_api.route("/")
def helloRest():
    return "Hello Rest"
