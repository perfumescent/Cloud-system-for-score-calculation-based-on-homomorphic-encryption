from flask import Flask
from flask import escape
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s\n%s' % (escape(name),name)