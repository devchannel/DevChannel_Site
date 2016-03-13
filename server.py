import json

import flask
import requests

import server_config
from apps import invite

app = flask.Flask(__name__)
app.secret_key = server_config.SERVER_SECRET


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


@app.route('/_login')
def login():
    uri = 'https://github.com/login/oauth/authorize' \
          '?scope={}&client_id={}'.format(server_config.GIT_SCOPE, server_config.GIT_CLIENT_ID)
    return flask.redirect(uri, code=302)


@app.route('/_callback')
def auth():
    session_code = flask.request.args.get('code')

    if session_code != '':
        resp = requests.post(
            'https://github.com/login/oauth/access_token',
            data={
                'client_id': server_config.GIT_CLIENT_ID,
                'client_secret': server_config.GIT_CLIENT_SECRET,
                'code': session_code
            },
            headers={
                'accept': 'application/json'
            }
        )
        if resp.status_code == 200:
            resp = json.loads(resp.text)
            if resp.get('scope') == 'user:email':
                acc_info = requests.get('https://api.github.com/user',
                                        params={'access_token': resp.get('access_token')})
                if acc_info.status_code == 200:
                    acc_info = json.loads(acc_info.text)
                    flask.session['username'] = acc_info.get('login')

                    return flask.redirect(flask.url_for('index'))

    return 'Something went wrong'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, threaded=True)
