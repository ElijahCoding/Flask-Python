from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:8889/fresh"
db = SQLAlchemy(app)

class Example(db.Model):
    __tablename__ = 'example'

    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Unicode)

    def __init__(self, id, data):
        self.id = id
        self.data = data


'''
# Add
from alchemy import Example, db
new_ex = Example(5, 'test-5')
db.session.add(new_ex)
db.session.commit()

# Update
update_ex = Example.query.filter_by(id=3).first()
update_ex.data = 'updated'
db.session.commit()

# Delete
delete_ex = Example.query.filter_by(id=2).first()
db.session.delete(delete_ex)
db.session.commit()
'''