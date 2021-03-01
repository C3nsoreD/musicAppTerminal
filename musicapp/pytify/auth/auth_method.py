from enum import Enum, auto


class AuthMethod(Enum):
    """ Authentication methods
            Client_credentials: requests for access token given user credentials. 
            Authorization_code
    """
    # auto() a helper that selects a value for enum memeber.
    CLIENT_CREDENTIALS = auto()
    AUTHORIZATION_CODE = auto()
