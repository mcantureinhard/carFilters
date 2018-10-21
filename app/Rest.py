from flask import Blueprint
from flask import Response
from flask import request
from flask import jsonify
from app import app
from json import dumps
from app.pipelines.questionsData import QuestionsData

rest_api = Blueprint('rest_api', __name__)

@rest_api.route("/")
def helloRest():
    return "Hello Rest"


#I'll just define this here for now
def questions_data(answers):
    state = {"answers" : answers}
    pipeline = QuestionsData(state=state)
    result = pipeline.executePipeline()
    return result

@rest_api.route("/question_aggs", methods=["POST"])
def question_aggs():
    content = request.get_json()
    if "answers" not in content:
        abort(500)
    result = questions_data(content["answers"])
    return jsonify({"filters" : result["aggs"]}), 200

@rest_api.route("/question_cars", methods=["POST"])
def question_cars():
    content = request.get_json()
    if "answers" not in content:
        abort(500)
    result = questions_data(content["answers"])
    return jsonify({"car_list" : result["avAgg"]}),200

@rest_api.route("/question_both", methods=["POST"])
def question_both():
    content = request.get_json()
    if "answers" not in content:
        abort(500)
    result = questions_data(content["answers"])
    return jsonify({"car_list" : result["avAgg"], "filters" : result["aggs"]}), 200