import os

from flask import Flask, render_template, redirect, url_for
from forms import commentForm

from models import Comment
from database import db_session
from flask import request

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = commentForm()
    if form.validate_on_submit():
        comment = Comment(ip=str(request.remote_addr),
                          comment=form.comment.data)
        db_session.add(comment)
        db_session.commit()
    comments = Comment.query.all()
    return render_template('index.html', comments=comments, form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5090, debug=False)
