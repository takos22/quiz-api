from flask_restful import Resource
import random

questions = {
    # "id": {"question": "Question?", "choices": ["1", "2", "3"], "answer": "3"}
    "1": {"question": "Question 1?", "choices": ["1", "2", "3"], "answer": "3"},
    "2": {"question": "Question 2?", "choices": ["4", "5", "6"], "answer": "5"},
}


class Question(Resource):
    def get(self):
        question_id = random.choice(list(questions.keys()))
        question = questions[question_id]
        return {"id": question_id, "question": question["question"], "choices": question["choices"]}


class Answer(Resource):
    def get(self, question_id: str):
        question = questions[question_id]
        return {"id": question_id, "answer": question["answer"]}
