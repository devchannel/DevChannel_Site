from flask_admin.contrib.sqla import ModelView
import flask
from .. import server_config


class AdminPost(ModelView):
    def is_accessible(self):
        return flask.session.get('username') in server_config.ALLOWED_USERS
