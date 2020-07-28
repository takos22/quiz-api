import unittest
import requests
import random


class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:5000"

    def test_question(self):
        # question
        r_question = requests.get(self.URL + "/question")
        # status code
        self.assertEqual(r_question.status_code, 200)
        # type
        self.assertEqual(type(r_question.json()), dict)
        # keys
        self.assertIn("id", r_question.json().keys())
        self.assertIn("question", r_question.json().keys())
        self.assertIn("choices", r_question.json().keys())
        # values type
        self.assertEqual(type(r_question.json()["id"]), str)
        self.assertEqual(type(r_question.json()["question"]), str)
        self.assertEqual(type(r_question.json()["choices"]), list)
        # values content
        self.assertTrue(r_question.json()["id"].isdigit())
        self.assertGreater(len(r_question.json()["question"]), 0)
        self.assertGreater(len(r_question.json()["choices"]), 0)

        # answer
        r_answer = requests.get(self.URL + f"/answer/{r_question.json()['id']}")
        # status code
        self.assertEqual(r_answer.status_code, 200)
        # type
        self.assertEqual(type(r_answer.json()), dict)
        # keys
        self.assertIn("id", r_answer.json().keys())
        self.assertIn("answer", r_answer.json().keys())
        # values type
        self.assertEqual(type(r_answer.json()["id"]), str)
        self.assertEqual(type(r_answer.json()["answer"]), str)
        # values content
        self.assertTrue(r_answer.json()["id"].isdigit())
        self.assertGreater(len(r_answer.json()["answer"]), 0)
        self.assertIn(r_answer.json()["answer"], r_question.json()["choices"])

    def test_question_category(self):
        # question
        r_question = requests.get(self.URL + "/question/1")
        # status code
        self.assertEqual(r_question.status_code, 200)
        # type
        self.assertEqual(type(r_question.json()), dict)
        # keys
        self.assertIn("id", r_question.json().keys())
        self.assertIn("question", r_question.json().keys())
        self.assertIn("choices", r_question.json().keys())
        # values type
        self.assertEqual(type(r_question.json()["id"]), str)
        self.assertEqual(type(r_question.json()["question"]), str)
        self.assertEqual(type(r_question.json()["choices"]), list)
        # values content
        self.assertTrue(r_question.json()["id"].isdigit())
        self.assertGreater(len(r_question.json()["question"]), 0)
        self.assertGreater(len(r_question.json()["choices"]), 0)

        # answer
        r_answer = requests.get(self.URL + f"/answer/{r_question.json()['id']}")
        # status code
        self.assertEqual(r_answer.status_code, 200)
        # type
        self.assertEqual(type(r_answer.json()), dict)
        # keys
        self.assertIn("id", r_answer.json().keys())
        self.assertIn("answer", r_answer.json().keys())
        # values type
        self.assertEqual(type(r_answer.json()["id"]), str)
        self.assertEqual(type(r_answer.json()["answer"]), str)
        # values content
        self.assertTrue(r_answer.json()["id"].isdigit())
        self.assertGreater(len(r_answer.json()["answer"]), 0)
        self.assertIn(r_answer.json()["answer"], r_question.json()["choices"])

    def test_question_category_404(self):
        # question
        r_question = requests.get(self.URL + "/question/0")
        # status code
        self.assertEqual(r_question.status_code, 404)
        # type
        self.assertEqual(type(r_question.json()), dict)
        # keys
        self.assertIn("message", r_question.json().keys())
        # values type
        self.assertEqual(type(r_question.json()["message"]), str)
        # values content
        self.assertGreater(len(r_question.json()["message"]), 0)
        self.assertRegex(
            r_question.json()["message"],
            r"Provided category_id \(\d+\) doesn't exist. For a list of available categories, go to https://github.com/takos22/quiz-api#categories",
        )

    def test_answer_404(self):
        # question
        r_answer = requests.get(self.URL + "/answer/0")
        # status code
        self.assertEqual(r_answer.status_code, 404)
        # type
        self.assertEqual(type(r_answer.json()), dict)
        # keys
        self.assertIn("message", r_answer.json().keys())
        # values type
        self.assertEqual(type(r_answer.json()["message"]), str)
        # values content
        self.assertGreater(len(r_answer.json()["message"]), 0)
        self.assertRegex(r_answer.json()["message"], r"Provided question_id \(\d+\) doesn't exist.")


if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit:
        pass
