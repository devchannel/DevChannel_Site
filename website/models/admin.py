from flask_admin.contrib.sqla import ModelView
import flask
from .. import server_config


class AdminPost(ModelView):
    edit_template = 'admin/post.html'
    create_template = 'admin/post.html'

    def is_accessible(self):
        return flask.session.get('username') in server_config.ALLOWED_USERS
