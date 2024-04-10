#!/usr/bin/env python3
"""
Instantiate the Babel object in your app. Store it in a module-level
variable named babel.In order to configure available languages in our app,
you will create a Config class that has a LANGUAGES class
attribute equal to ["en", "fr"].
Use Config to set Babel’s default locale ("en") and timezone ("UTC").
Use that class as config for your Flask app.
"""

from flask import Flask, render_template
from werkzeug.utils import cached_property
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    babel.BABEL_DEFAULT_LOCALE = "en"
    babel.BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    """ return index.html """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
