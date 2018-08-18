#!/usr/bin/env python3

from urllib import request
import json


def locations():
    return {
        'Sloss Furnace': 223556,
        'Railroad Park': 1579486,
    }


def _get_client_info():
    with open('etc/instagram.txt') as f:
        client_id = f.readline().strip()
        secret = f.readline().strip()
    return (client_id, secret)


def _get_user_info():
    with open('etc/insta-user.txt') as f:
        username = f.readline().strip()
        password = f.readline().strip()
        code = f.readline().strip()
        token = f.readline().strip()
    return (username, password, code, token)


def recent_location_media(location_str):
    location_ids = locations()
    location_id = location_ids.get(location_str)
    if not location_id:
        location_id = locations.get('Sloss Furnace')
    params = 'locations/' + str(location_id)
    return _request({'command': 'media/recent', 'params': params})


def _request(args):
    command = args.get('command')
    params = args.get('params')
    user_info = _get_user_info()
    token = user_info[3]
    endpoint = 'https://api.instagram.com/v1'
    url = '/'.join([endpoint, params, command])
    url += '?access_token=' + token
    f = request.urlopen(url)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    f.close()
    return parsed_json


def get_media_urls():
    #  Returns a list of urls where images are located
    response = recent_location_media('Sloss Furnace')
    data = response.get('data')
    urls = []
    for item in data:
        images = item.get('images')
        image_info = images.get('standard_resolution')
        image_url = image_info.get('url')
        if image_url:
            urls.append(image_url)
    return urls


def get_test_media():
    print(get_media_urls())
    return
