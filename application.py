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

from .helpers import timepractice, instagram, bulletin_picker, wunderground

app = Flask(__name__)

@app.route('/')
def homepage():
    """ Render the homepage. """
    the_gif = timepractice.gif_picker()
    insta = instagram.get_recent_instagram()
    bulletin_info = bulletin_picker.bulletin_picker()
    colorscheme = bulletin_info[1]
    bulletin_text = bulletin_info[0]

    wunderground.watch_temps() # do a little data wactching. Just because

    return render_template(
        'index.html',
        gif=the_gif,
        instagram=insta,
        colorscheme=colorscheme,
        bulletin_text=bulletin_text
    )

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
