from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

from api import resources, models

api.add_resource(resources.Question, "/question", "/question/<int:category_id>")
api.add_resource(resources.Answer, "/answer/<int:question_id>")
api.add_resource(resources.Category, "/category/<int:category_id>")
api.add_resource(resources.Category.All, "/category/all")
