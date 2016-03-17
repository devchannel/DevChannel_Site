import flask

import server_config
from apps import invite, database

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/index')
def dummy_index():
    # TODO: fix this shit later
    return index()


@app.route('/docs')
def docs():
    return flask.render_template('docs.html')


@app.route('/about')
def about():
    return flask.render_template('about.html')


@app.route('/resources')
def resources():
    return flask.render_template('resources.html')


@app.route('/join', methods=['GET', 'POST'])
def join():
    if flask.request.method == 'POST':
        email = flask.request.form['email']
        p_langs = flask.request.form['p_langs']

        # redir: -1, 0 or 1
        # -1: stay on page;    0: redirect to index.html;    1: redirect to slack
        if email == '' or p_langs == '':
            redir, resp = -1, 'Please fill every field!'
        else:
            redir, resp = invite.send_invite(email, p_langs)

        return flask.render_template('join.html', status=redir, rep_error=resp)
    else:
        return flask.render_template('join.html', status=None, rep_error=None)


@app.route('/_database', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _database():
    if flask.session.get('username') not in server_config.ALLOWED_USERS:
        return 'Unauthorized'

    langs = flask.request.args.get('langs', '')
    email = flask.request.args.get('email', '')
    username = flask.request.args.get('username', '')
    slack_id = flask.request.args.get('slack_id', '')
    git = flask.request.args.get('git', '')
    timezone = flask.request.args.get('timezone', '')

    req_all = flask.request.args.get('all', '')

    if flask.request.method == 'POST':
        return database.insert_user(email=email, username=username, slack_id=slack_id,
                                    langs=langs, git=git, timezone=timezone)

    elif flask.request.method == 'PUT':
        params = {}
        if langs != '':
            params['skills'] = langs
        if git != '':
            params['github'] = git
        if timezone != '':
            params['time'] = timezone
        if username != '' and email != '':
            params['name'] = username
        return database.update_user(email=email, username=username, slack_id=slack_id, params=params)

    elif flask.request.method == 'GET':
        if req_all == '':
            return database.get_all_users()
        return database.get_user(email=email, username=username, slack_id=slack_id)

    elif flask.request.method == 'DELETE':
        return database.delete_user(email=email, username=username, slack_id=slack_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, threaded=True)
