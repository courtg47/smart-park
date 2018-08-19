
import time

import datetime

from datetime import datetime

from helpers import wunderground

current_month = datetime.now().month
current_hour = datetime.now().minute


def gif_picker():

    if current_hour >= 20:
        gif = 'IMG_0023.GIF'
        return gif
    
    elif current_month == 12:
        gif = 'IMG_0024.GIF'
        return gif

    '''elif sunny
        return sunnygif

    elif cloudy
        return cloudygif'''
print(wunderground.get_weather())





