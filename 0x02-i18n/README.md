# 0x02. i18n

## Overview
This repository hosts a comprehensive guide to internationalization (i18n) in Flask applications. The primary focus is on implementing multilingual support and localization features. The project is structured around several tasks, each building upon the previous one to achieve a fully internationalized Flask application.

## Project Details
- **Start Date:** April 9, 2024
- **End Date:** April 13, 2024
- **Status:** Ongoing
- **Manual QA Review:** Scheduled after the second deadline
- **Auto QA Review:** 0.0/48 mandatory checks completed
- **Reviews Pending:** Waiting on some reviews

## Learning Objectives
- Understand how to parametrize Flask templates for displaying content in different languages.
- Learn methods to infer the correct locale based on various factors such as URL parameters, user settings, or request headers.
- Implement localization of timestamps to adapt to different time zones.

## Requirements
- All code should be executed on Ubuntu 18.04 LTS using Python 3.7.
- Files should adhere to PEP 8 style guidelines (pycodestyle).
- Scripts should start with `#!/usr/bin/env python3` and be executable.
- Documentation should be provided for modules, classes, functions, and methods.
- Functions and coroutines must be type-annotated.
- Each function, class, or module should have a meaningful documentation explaining its purpose.
- A `README.md` file is mandatory for the project.

## Tasks
1. **Basic Flask App**
   - Set up a basic Flask application with a single route and a simple HTML template.
   - GitHub Repository: [alx-backend](https://github.com/alx-backend)
   - File: `0x02-i18n/0-app.py`, `0x02-i18n/templates/0-index.html`

2. **Basic Babel Setup**
   - Install the Flask Babel extension and configure language settings.
   - File: `0x02-i18n/1-app.py`, `0x02-i18n/templates/1-index.html`

3. **Get Locale from Request**
   - Implement a function to determine the best match for the user's preferred language.
   - File: `0x02-i18n/2-app.py`, `0x02-i18n/templates/2-index.html`

4. **Parametrize Templates**
   - Use gettext to parametrize templates for multilingual support.
   - File: `0x02-i18n/3-app.py`, `0x02-i18n/babel.cfg`, `0x02-i18n/templates/3-index.html`, `0x02-i18n/translations/*`

5. **Force Locale with URL Parameter**
   - Implement a way to force a particular locale via URL parameters.
   - File: `0x02-i18n/4-app.py`, `0x02-i18n/templates/4-index.html`

6. **Mock Logging In**
   - Mock a user login system to emulate user-specific localization settings.
   - File: `0x02-i18n/5-app.py`, `0x02-i18n/templates/5-index.html`

7. **Use User Locale**
   - Update to use a user's preferred locale if available.
   - File: `0x02-i18n/6-app.py`, `0x02-i18n/templates/6-index.html`

8. **Infer Appropriate Time Zone**
   - Define a function to infer the appropriate time zone for users.
   - File: `0x02-i18n/7-app.py`, `0x02-i18n/templates/7-index.html`

## Resources
- [Flask-Babel](https://flask-babel.tkte.ch/)
- [Flask i18n Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
- [pytz](http://pytz.sourceforge.net/)

---
This README serves as a guide to understand and navigate through the i18n project. For detailed implementation and code instructions, refer to individual files within the project directory.
