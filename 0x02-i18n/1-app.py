#!/usr/bin/env python3
"""
This module defines a Flask app with Babel integration.
"""

from flask import Flask, render_template
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


@app.route('/')
def index():
    """
    Render the index.html template.
    """
    return render_template('1-index.html', title='Welcome to Holberton', header='Hello world')


if __name__ == "__main__":
    app.run(debug=True)