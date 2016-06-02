from functools import wraps

from .. import server_config

import flask


def must_login(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if flask.session.get('username') not in server_config.ALLOWED_USERS:
            flask.abort(403)

        result = f(*args, **kwargs)
        return result
    return wrapper
