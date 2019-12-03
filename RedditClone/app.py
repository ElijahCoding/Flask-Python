from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:8889/fresh'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'working'

if __name__ == '__main__':
    app.run(debug=True)