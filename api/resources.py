from flask_restful import Resource
import random

categories = {
    # "id": {"name": "Category name"}
    "1": {"name": "Tech"},
}

questions = {
    # "id": {"question": "Question?", "choices": ["1", "2", "3"], "answer": "3", "category_id": "1"}
    "1": {"question": "Question 1?", "choices": ["1", "2", "3"], "answer": "3"},
    "2": {"question": "Question about tech?", "choices": ["4", "5", "6"], "answer": "5", "category_id": "1"},
}


class Question(Resource):
    def get(self, category_id: str = None):
        question_id = random.choice(
            [
                key for key, question in questions.items()
                if "category_id" in question.keys() and question["category_id"] == category_id
            ]
            if category_id
            else list(questions.keys())
        )
        question = questions[question_id]
        return {"id": question_id, "question": question["question"], "choices": question["choices"]}


class Answer(Resource):
    def get(self, question_id: str):
        question = questions[question_id]
        return {"id": question_id, "answer": question["answer"]}
