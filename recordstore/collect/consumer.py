import json

import requests
from django.conf import settings

CONSUMER_USER_AGENT = 'RecordStore Discogs Consumer'
DISCOGS_API_URL = 'https://api.discogs.com'
DISCOGS_API_TOKEN = settings.DISCOGS_TOKEN

def database_search_barcode(barcode):
    """
    Searches Discogs database for barcode
    """
    return call(path='/database/search', params={'barcode': barcode})

def database_release(release_id):
    """
    Fetches release from Discogs database
    """
    return call(path='/releases/{}'.format(release_id))

def call(path, params={}):
    """
    Calls the Discogs API and returns results as object
    """
    url = DISCOGS_API_URL + path
    params['token'] = DISCOGS_API_TOKEN
    headers = {
        'User-Agent': CONSUMER_USER_AGENT,
    }

    response = requests.get(url, params=params, headers=headers)
    print response.status_code
    return json.loads(response.content)