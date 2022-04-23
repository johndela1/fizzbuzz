#!/usr/bin/env python3

import requests

from urllib.parse import urlencode

def find_definition(word):
    q = f'define {word}'
    url = f'http://api.duckduckgo.com/?'
    url += urlencode(dict(q=q, format='json'))
    data = call_json_api(url)
    definition = data['meta']['src_url']
    if not definition:
        raise ValueError('that is not a word')
    return definition


def call_json_api(url):
    response = requests.get(url)
    data = response.json()
    return data

print(find_definition('hey'))
