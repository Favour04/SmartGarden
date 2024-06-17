from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return f'Index page!'

@app.route('/hello')
def hello_worl():
    return "<p><strong>Hello world</strong></P>"

@app.route('/project/')
def project():
    return "The project Page"

@app.route('/user/<username>')
def profile(username):
    return f"{username}'s profile"
