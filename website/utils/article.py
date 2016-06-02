import os
import datetime

import tinydb

db = tinydb.TinyDB(os.path.join(os.path.dirname(__file__), '..', 'database/articles.json'))


class Article:
    def __init__(self, author, text, publish_date=None):
        self.author = author
        self.text = text
        if publish_date is None:
            publish_date = str(datetime.datetime.now().date())
        self.publish_date = publish_date

    def __repr__(self):
        return str({'author': self.author, 'text': self.text, 'publish_date': self.publish_date})


def get_articles():
    return db.all()


def save_article(obj):
    db.insert(obj.__dict__)
