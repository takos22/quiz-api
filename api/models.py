from api import app, db
import json

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String())
    choices = db.Column(db.String())  # list in a str (json) ex: '["1", "2", "3"]'
    answer = db.Column(db.String())
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))

    def __repr__(self):
        return f"<Question id={self.id} question='{self.question}' choices={json.loads(self.choices)} answer='{self.answer}' category={self.category}>"

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    questions = db.relationship("Question", backref="category", lazy="dynamic")

    def __repr__(self):
        return f"<Category id={self.id} name='{self.name}'>"
