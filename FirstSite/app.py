import flask

from infrastructure.view_modifiers import response
from services.package_service import get_latest_packages

app = flask.Flask(__name__)

@app.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = get_latest_packages()
    return {"packages": test_packages}

@app.route('/about')
@response(template_file='home/about.html')
def about():
    return flask.render_template('home/about.html')

if __name__ == '__main__':
    app.run(debug=True)