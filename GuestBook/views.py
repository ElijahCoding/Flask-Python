from flask import url_for, Blueprint, render_template, request, redirect
from .models import Comment
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    comments = Comment.query.all()
    return render_template('index.html', comments=comments)

@main.route('/sign')
def sign():
    return render_template('sign.html')

@main.route('/sign', methods=['POST'])
def sign_post():
    name = request.form.get('name')
    comment = request.form.get('comment')

    new_comment = Comment(name=name, comment_text=comment)
    db.session.add(new_comment)
    db.session.commit()

    return redirect(url_for('main.index'))
