import datetime

from .. import db


def get_curr_date():
    return datetime.datetime.now().date()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    visible = db.Column(db.Boolean, default=False)
    author = db.Column(db.String(20), default='therightman')
    publish_date = db.Column(db.Date, default=get_curr_date)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def __init__(self, visible=None, author="", date="", title="", text=""):
        self.visible = visible
        self.author = author
        self.publish_date = date
        self.title = title
        self.text = text

    def __repr__(self):
        return str({'author': self.author, 'text': self.text, 'publish_date': self.publish_date})
