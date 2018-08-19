#!/usr/bin/env python3

"""
This is the main python application for the Smart Park project.
"""

# Importing Flask
from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    url_for
)

from helpers import timepractice, instagram

app = Flask(__name__)

@app.route('/')
def homepage():
    """ Render the homepage. """
    the_gif = timepractice.gif_picker()
    insta = instagram.get_recent_instagram()

    return render_template('index.html', gif=the_gif, instagram=insta)

if __name__ == '__main__':
    app.debug = True
    app.run()
