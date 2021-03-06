
import time

import datetime

from datetime import datetime

from . import wunderground


def gif_picker():

    current_month = datetime.now().month
    current_hour = datetime.now().hour
    current_weather = wunderground.get_weather()

    if current_hour >= 20:
        gif = 'IMG_0023.GIF'
        return gif

    elif current_month == 12:
        gif = 'IMG_0024.GIF'
        return gif

    elif current_weather is 'Overcast' or 'Mostly Cloudy' or 'Heavy Rain' or 'Light Rain':
        gif = 'IMG_0022.GIF'
        return gif

    else:
        gif = 'IMG_0021.GIF'
        return gif


print(gif_picker())
