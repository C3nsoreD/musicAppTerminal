from .config import read_config
from .exceptions import BadRequestError

from .search_type import SearchType

from .search import search_album
from .search import search_playlist
from .search import search_track
from .search import search_artist

from .artists import get_artist_album
from .album import get_album_tracks
from .player import play
