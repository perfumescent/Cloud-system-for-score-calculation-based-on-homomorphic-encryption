from flask import Flask, render_template, escape
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s\n%s' % (escape(name),name)