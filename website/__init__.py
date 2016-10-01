from urllib.parse import urlparse, urlunparse
import flask
from flaskext.markdown import Markdown
from flask_sqlalchemy import SQLAlchemy
import flask_admin

from . import server_config

app = flask.Flask(__name__)
app.secret_key = server_config.SERVER_SECRET

Markdown(app)

app.config['SQLALCHEMY_DATABASE_URI'] = server_config.ARTICLE_DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SERVER_NAME'] = server_config.HOST_NAME
db = SQLAlchemy(app)

from .models.posts import Post
from .models.admin import AdminPost
admin = flask_admin.Admin(app, name='ADMIN')
admin.add_view(AdminPost(Post, db.session))

from .server import *

@app.before_request
def redir_to_non_www():
    url = urlparse(flask.request.url)
    if url.netloc.startswith("www."):
        url_parts = list(url)
        url_parts[1] = url_parts[1][4:]
        k = urlunparse(url_parts)
        return flask.redirect(k, code=301)

from website import subdomains
for attr in dir(subdomains):
    if not attr.startswith('__'):
        bprint = getattr(subdomains, attr)
        app.register_blueprint(bprint)
