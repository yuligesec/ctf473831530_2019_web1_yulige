import flask
import os
app = flask.Flask(__name__)
app.config['HINT'] = os.environ.pop('HINT')
@app.route('/')
def index():
    return open(__file__).read()
@app.route('/yulige/<path:yulige>')
def yulige(yulige):
    def safe_jinja(s):
        s = s.replace('(', '').replace(')', '')
        blacklist = ['config', 'self']
        return ''.join(['{{% set {}=None%}}'.format(c) for c in blacklist])+s
    return flask.render_template_string(safe_jinja(yulige))
if __name__ == '__main__':
    app.run("0.0.0.0",port=8080)
