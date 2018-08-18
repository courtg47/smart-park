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

app = Flask(__name__)

@app.route('/')
def homepage():
    """ Render the homepage. """
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
