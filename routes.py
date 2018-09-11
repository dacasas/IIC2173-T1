from flask import render_template, flash, redirect
from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from app.models import Comment
from app import db
from flask import request

class commentForm(FlaskForm):
    comment = StringField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = commentForm()
    if form.validate_on_submit():
        comment = Comment(ip=str(request.remote_addr), comment=form.comment.data)
        db.session.add(comment)
        db.session.commit()
    comments = Comment.query.all()
    return render_template('index.html', comments=comments, form=form)
