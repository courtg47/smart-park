#!/usr/bin/env python3
from urllib import request
import json


def get_weather_data():
    endpoint = 'http://api.wunderground.com/api'
    command = 'geolokup/conditions/q/AL/Birmingham.json'
    key = _get_credentials()
    url = '/'.join([endpoint, key, command])
    f = request.urlopen(url)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    f.close()
    return parsed_json


def _get_credentials():
    with open('etc/wunderground.txt') as f:
        key = f.readline()
    return key
