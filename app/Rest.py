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
    return jsonify({"filters" : result["filters"]}), 200

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
    return jsonify({"car_list" : result["avAgg"], "filters" : result["filters"]}), 200


#Dummy questions end point
@rest_api.route("/easy_filter_questions", methods=["GET"])
def get_questions():
    #I'd like to say I'll implement these questions dynamically in the FE, but for now, even though I am adding type, 
    #I will make the FE static
    questions = [
        {'question' : "For how many people do you need this car?", "type" : "boxe", "options" : [1,2,3,4,5,6,7,8]},
        {'question' : "Which type of insurance do you need?", "type" : "radio_box", "options" : ["Basic Insurance", "Good Insurance", "Premium Insurance"]},
        {'question' : "Do you want to have the best fuel option?", "type" : "radio_box", "options" : ["Yes", "No"]},
    ]
    return jsonify({"questions": questions}), 200
