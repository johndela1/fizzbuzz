#!/usr/bin/env python3

import requests

from urllib.parse import urlencode

def find_definition(word):
    return extract(requests.get(build_url(word)).json())


def extract(data):
    definition = data['meta']['src_url']
    if not definition:
        raise ValueError('that is not a word')
    return definition


def build_url(word):
    q = f'define {word}'
    return f'http://api.duckduckgo.com/?{urlencode(dict(q=q, format="json"))}'

print(find_definition('hey'))
