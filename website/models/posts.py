import datetime

from .. import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(20))
    publish_date = db.Column(db.Date)
    text = db.Column(db.Text)

    def __init__(self, author="", date="", text=""):
        self.author = author
        self.publish_date = date or datetime.datetime.now().date()
        self.text = text

    def __repr__(self):
        return str({'author': self.author, 'text': self.text, 'publish_date': self.publish_date})
