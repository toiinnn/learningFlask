from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Antonio', 'email': 'antonio@email.com'}
    posts = [
        {
            'author': {'username': 'John', 'email': 'john@email.com'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan', 'email': 'susan@email.com'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

    
