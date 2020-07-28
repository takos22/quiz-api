from flask_restful import Resource, abort
import random

categories = {
    # "id": {"name": "Category name"}
    "1": {"name": "Tech"},
    "2": {"name": "Science"},
    "3": {"name": "Sports"},
}

questions = {
    # "id": {"question": "Question?", "choices": ["1", "2", "3"], "answer": "3", "category_id": "1"}
    "1": {"question": "Question 1?", "choices": ["1", "2", "3"], "answer": "3"},
    "2": {"question": "Question about tech?", "choices": ["4", "5", "6"], "answer": "5", "category_id": "1"},
    "3": {"question": "Question about science?", "choices": ["7", "8", "9"], "answer": "7", "category_id": "2"},
    "4": {"question": "Question about sports?", "choices": ["10", "11", "12"], "answer": "12", "category_id": "3"},
}


class Question(Resource):
    def get(self, category_id: str = None):
        if category_id is not None and category_id not in categories.keys():
            abort(
                404,
                message="Provided category_id doesn't exist. For a list of available categories, go to https://github.com/takos22/quiz-api#categories",
                status="404",
            )

        question_id = random.choice(
            [key for key, question in questions.items() if "category_id" in question.keys() and question["category_id"] == category_id]
            if category_id
            else list(questions.keys())
        )
        question = questions[question_id]
        return {"id": question_id, "question": question["question"], "choices": question["choices"]}


class Answer(Resource):
    def get(self, question_id: str):
        if question_id is not None and question_id not in questions.keys():
            abort(
                404, message="Provided question_id doesn't exist.", status="404",
            )

        question = questions[question_id]
        return {"id": question_id, "answer": question["answer"]}
