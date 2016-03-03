import flask

from apps import invite

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

        return invite.send_invite(email, p_langs)
    else:
        return flask.render_template('join.html')

if __name__ == '__main__':
    app.run()
