#!/usr/bin/env python3
"""
Logging in will be mocked by passing login_as URL parameter
containing the user ID to log in as.
Define a get_user function that returns a user dictionary or
None if the ID cannot be found or if login_as was not passed.
Define a before_request function and use the app.before_request
decorator to make it be executed before all other functions.
before_request should use get_user to find a user if any, and
set it as a global on flask.g.user.
In your HTML template, if a user is logged in, in a paragraph tag,
display a welcome message otherwise display a default message as
shown in the table below.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """ Returns a user dictionary or None if the ID cannot be found """
    try:
        login_as = request.args.get('login_as')
        user_id = int(login_as)
        return users[user_id]
    except Exception:
        return None


@app.before_request
def before_request():
    """ Executed before all other functions """
    user = get_user()
    if user:
        g.user = user


# @babel.localeselector
def get_locale():
    """ Get locale """
    user = get_user()
    if user:
        locale = user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index():
    """ Returns index """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
