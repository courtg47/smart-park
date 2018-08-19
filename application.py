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

from helpers import timepractice

app = Flask(__name__)

@app.route('/')
def homepage():
    """ Render the homepage. """
    # bulletin = helpers.bulletin
    the_gif = timepractice.gif_picker()

    return render_template('index.html', gif=the_gif)

if __name__ == '__main__':
    app.debug = True
    app.run()
