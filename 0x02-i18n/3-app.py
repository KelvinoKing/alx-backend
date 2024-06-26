#!/usr/bin/env python3
"""
Use the _ or gettext function to parametrize your templates.
Use the message IDs home_title and home_header
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ get locale """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index():
    """ Returns index """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
