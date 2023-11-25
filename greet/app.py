from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    """Return "Welcome!" Greeting."""
    return 'Welcome!'

@app.route('/welcome/home')
def welcome_home():
    """Return "Welcome home!" Greeting."""
    return "Welcome home!"

@app.route('/welcome/back')
def welcome_back():
    """Return "Welcome back!" Greeting."""
    return "Welcome back!"