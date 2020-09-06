from flask_restful import Resource, abort
from sqlalchemy.sql.expression import func
import json
from typing import List, Optional

from api import models


class Question(Resource):
    def get(self, category_id: Optional[int] = None):
        if category_id is not None:
            question: models.Question = (
                models.Question.query.filter_by(category_id=category_id)
                .order_by(func.random())
                .first_or_404(
                    description=f"Provided category_id ({category_id}) doesn't exist. "
                    "For a list of available categories, go to https://github.com/takos22/quiz-api#categories"
                )
            )
        else:
            question: models.Question = models.Question.query.order_by(func.random()).first()
        return {"id": question.id, "question": question.question, "choices": json.loads(question.choices)}


class Answer(Resource):
    def get(self, question_id: int):
        question: models.Question = models.Question.query.filter_by(id=question_id).first_or_404(
            description=f"Provided question_id ({question_id}) doesn't exist."
        )
        return {"id": question.id, "answer": question.answer}


class Category(Resource):
    def get(self, category_id: int):
        category: models.Category = models.Category.query.filter_by(id=category_id).first_or_404(
            description=f"Provided category_id ({category_id}) doesn't exist. "
            "For a list of available categories, go to https://github.com/takos22/quiz-api#categories"
        )
        return {"id": category.id, "name": category.name}

    class All(Resource):
        def get(self):
            categories: List[models.Category] = models.Category.query.all()
            return [{"id": category.id, "name": category.name} for category in categories]
