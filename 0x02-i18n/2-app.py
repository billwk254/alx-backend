#!/usr/bin/env python3
"""
This module defines a Flask app with Babel integration.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class to set available languages, default locale, and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale():
    """
    Get the best matching locale based on user's preferred languages.
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """
    Render the index.html template.
    """
    return render_template('2-index.html', title='Welcome to Holberton', header='Hello world')


if __name__ == "__main__":
    app.run(debug=True)
