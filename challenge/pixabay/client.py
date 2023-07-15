import requests
from django.conf import settings

base_url = 'https://pixabay.com/api'

def get(params):
    params['key'] = settings.KEY

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
    except requests.HTTPError as ex:
        print(ex)
    else:
        data = response.json()
        images = data.get('hits', None)
        return images
    return None
