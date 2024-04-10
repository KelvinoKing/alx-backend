#!/usr/bin/env python3
"""
Define a get_timezone function and use the
babel.timezoneselector decorator.
The logic should be the same as get_locale:
Find timezone parameter in URL parameters
Find time zone from user settings
Default to UTC
Before returning a URL-provided or user time zone,
you must validate that it is a valid time zone.
To that, use pytz.timezone and catch the 
pytz.exceptions.UnknownTimeZoneError exception.
"""

from flask import Flask, render_template, request, g
import pytz
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


@babel.localeselector
def get_locale():
    """ Get locale """
    user = get_user()
    if user:
        locale = user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ Get timezone """
    user = get_user()
    if user:
        timezone = user.get('timezone')
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


# babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/', strict_slashes=False)
def index():
    """ Returns index """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
