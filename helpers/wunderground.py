#!/usr/bin/env python3
from urllib import request
import json


def _get_weather_data():
    endpoint = 'http://api.wunderground.com/api'
    command = 'geolokup/conditions/q/AL/Birmingham.json'
    key = _get_credentials()
    key = key.strip()
    url = '/'.join([endpoint, key, command])
    f = request.urlopen(url)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    f.close()
    return parsed_json.get('current_observation')


def _get_credentials():
    with open('etc/wunderground.txt') as f:
        key = f.readline()
    return key

def clean_weather_info():
    print(get_temp())
    print(get_weather())
    return

def get_temp():
    raw = _get_weather_data()
    return raw.get('temp_f')

def get_weather():
    raw = _get_weather_data()
    return raw.get('weather')
