import request
import json
from urllib.parse import urlencode

from .search_type import SearchType
from pytify.core import read_config


def _search(criteria, auth, search_type):
     conf = read_config()

     # ensure a criteria has been passed
     if not criteria:
         raise AttributeError('Parameter `criteria` is required')

    # construct the query
    q_type = search_type.name.lower()
    url = urlencode(f'{conf.base_url}/search?q={criteria}&type={q_type}')
    headers = {'Authorization': f'Bearer {auth.access_token}'}
    response = request.get(url, headers=headers)

    return json.loads(response.text)

def search_artist(criteria, auth):
    return _search(criteria, auth, SearchType.ARTIST)

def search_playlist(criteria, auth):
    return _search(criteria, auth, SearchType.PLAYLIST)

def search_album(criteria, auth):
    return _search(criteria, auth, SearchType.ALBUM)

def search_track(criteria, auth):
    return _search(criteria, auth, SearchType.TRACK)
