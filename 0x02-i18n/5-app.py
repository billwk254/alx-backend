#!/usr/bin/env python3
"""
This module defines a Flask app with user login system mockup and internationalization support.
"""


from flask import Flask, render_template, g, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    """
    Get user data based on user ID.
    """
    return users.get(user_id)

@app.before_request
def before_request():
    """
    Get user data based on login_as URL parameter and set it as global on flask.g.user.
    """
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None

@babel.localeselector
def get_locale():
    """
    Get the best matching locale based on user's preferred languages.
    """
    if g.user and g.user['locale']:
        return g.user['locale']
    else:
        return request.accept_languages.best_match(['en', 'fr'])

@app.route('/')
def index():
    """
    Render the index.html template.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
