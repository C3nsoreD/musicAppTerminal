from .parameter import prepare_params
from .request import execute_request


def get_artist_album(artist_id, auth, params=None):
    # Validation
    if artist_id is None or artist_id is "":
        raise AttributeError(
            "Parameter `artist_id` is empty or is `None`"
        )
    # construction of url
    url_template = '{base_url}/{area}/{artistid}/{postfix}{query}'
    url_params = {
        'query' : prepare_params(params),
        'area' : 'artist',
        'artistid': artist_id,
        'postfix': 'album'
    }

    return execute_request(url_template, auth, url_params)
