import flask
from views import home_views

app = flask.Flask(__name__)

def main():
    register_blueprints()
    app.run(debug=True)

def register_blueprints():
    app.register_blueprint(home_views.blueprint)

if __name__ == '__main__':
    main()