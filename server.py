import flask

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
    langs = flask.request.args.get('langs', '')
    email = flask.request.args.get('email', '')
    username = flask.request.args.get('username', '')
    git = flask.request.args.get('!github', '')
    timezone = flask.request.args.get('timezone', '')

    if flask.request.method == 'POST':
        return database.insert_user(langs=langs, email=email, username=username, git=git, timezone=timezone)

    elif flask.request.method == 'PUT':
        params = {}
        if langs != '':
            params['!skills'] = langs
        if git != '':
            params['!github'] = git
        if timezone != '':
            params['!time'] = timezone
        return database.update_user(email=email, username=username, params=params)

    elif flask.request.method == 'GET':
        return database.get_user(email=email, username=username)

    elif flask.request.method == 'DELETE':
        return database.delete_user(email=email, username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, threaded=True)
