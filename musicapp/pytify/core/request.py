import requests
import json

from .exceptions import BadRequestError
from .config import read_config
from .request_type import RequestType


def execute_request(url_template, auth, params, request_type=RequestType.GET, payload=()):
    
