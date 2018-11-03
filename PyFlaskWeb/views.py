"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, render_template
from PyFlaskWeb import app
from flask_sqlalchemy import SQLAlchemy

app.config.from_pyfile('hello.cfg')
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column('todo_id', db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    text = db.Column(db.String)
    done = db.Column(db.Boolean)
    pub_date = db.Column(db.DateTime)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.done = False
        self.pub_date = datetime.utcnow()




@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    all=0
    pak4=0
    pak5=0
    pak6=0
    pak7=0
    pak8=0
    pak9=0
    pak10=0
    pak11=0
    pak12=0
    resultall=all + pak4 + pak5 + pak6 + pak7 + pak8 + pak9 + pak10 + pak11 + pak12
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        todos=Todo.query.order_by(Todo.pub_date.desc()).all(),
        all=all, 
        pak4=pak4, 
        pak5=pak5, 
        pak6=pak6, 
        pak7=pak7, 
        pak8=pak8, 
        pak9=pak9, 
        pak10=pak10, 
        pak11=pak11,
        pak12=pak12, 
        resultall = resultall
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message=''
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message=''
    )


@app.route('/install')
def install():
    return render_template(
        'install.html',
        title='install',
        year=datetime.now().year,
        message='...'
        )
@app.route('/realinstall')
def realinstall():
    return render_template(
        'realinstall.html',
        title='realinstall',
        year=datetime.now().year,
        message='real install.'
        )

@app.route('/resultinstall')
def resultinstall():
    return render_template(
        'resultinstall.html',
        title='resultinstall',
        year=datetime.now().year,
        message='result install'
        )