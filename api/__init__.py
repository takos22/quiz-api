from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from api.resources import Question, Answer

api.add_resource(Question, "/question")
api.add_resource(Answer, "/answer/<string:question_id>")
