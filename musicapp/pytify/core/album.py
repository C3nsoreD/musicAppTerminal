from .parameter import prepare_params
from .request import execute_request


def get_album_tracks(album_id, auth, params=None):
    if album_id is None or album_id is "":
        raise AttributeError(
            "Parameter `album_id` cannot be `None` or is Empty"
        )

    url_template = '{base_url}/{area}/{albumid}/{postfix}{query}'
    url_params = {
        'query' : prepare_params(params),
        'area': 'album',
        'albumid': album_id,
        'postfix': 'tracks',
    }
    return execute_request(url_template, auth, url_params)
