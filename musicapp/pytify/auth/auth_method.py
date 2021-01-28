from enum import Enum, auto

"""
Enum:

Symbolic names bound to unique, constant values

"""

class AuthMethod(Enum):
    # auto() a helper that selects a value for enum memeber.
    CLIENT_CREDENTIALS = auto()
    AUTHORIZATION_CODE = auto()
