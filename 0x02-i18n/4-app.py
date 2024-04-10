#!/usr/bin/env python3
"""
In this task, you will implement a way to force a particular locale
by passing the locale=fr parameter to your app’s URLs.
In your get_locale function, detect if the incoming request contains
locale argument and ifs value is a supported locale, return it.
If not or if the parameter is not present,
resort to the previous default behavior.
Now you should be able to test different translations by visiting
http://127.0.0.1:5000?locale=[fr|en].
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
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index():
    """ Returns index """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
