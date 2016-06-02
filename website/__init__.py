from urllib.parse import urlparse, urlunparse
import flask
from flaskext.markdown import Markdown

from . import server_config

app = flask.Flask(__name__)
Markdown(app)
app.secret_key = server_config.SERVER_SECRET

from .server import *


@app.before_request
def redir_to_non_www():
    url = urlparse(flask.request.url)
    if url.netloc.startswith("www."):
        url_parts = list(url)
        url_parts[1] = url_parts[1][4:]
        k = urlunparse(url_parts)
        return flask.redirect(k, code=301)
