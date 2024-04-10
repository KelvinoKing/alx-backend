#!/usr/bin/env python3
"""
Create a get_locale function with the babel.localeselector decorator.
Use request.accept_languages to determine the best match with our
supported languages
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ get locale """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """ Returns index """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
