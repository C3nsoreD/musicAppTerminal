import os
import yaml
from collections import namedtuple

from ..auth import AuthMethod

# Basic parameters required for configuration.
Config = namedtuple(
    'Config', [
        'client_id', 'client_secret', 'access_token_url', 'auth_url',
        'api_version', 'api_url', 'base_url', 'auth_method',
    ]
)

def read_config():
    current_dir = os.path.abspath(os.curdir)
    file_path = os.path.join(current_dir, 'config.yaml')

    try:
        with open(file_path, mode='r', encoding='UTF-8') as file:
            config = yaml.load(file)
            # creates base_url from Yaml config parameters.
            config['base_url'] = f'{config["api_url"]}/{config["api_version"]}'
            auth_method = config['auth_method']
            config['auth_method'] = AuthMethod.__members__.get(auth_method)

            # returns the config as a namedtuple object defined above.
            return Config(**config)

    # Reports errors in reading the file and provides instructions for possible fix.
    except IOError as e:
        print(""" Error: couldn''t find the config file
            `config.yaml` on your directory

            Default format is:',

            client_id: 'your_client_id'
            client_secret: 'your_client_secret'
            access_token_url: 'https://accounts.spotify.com/api/token'
            auth_url: 'https://accounts.spotify.com/authrize'
            api_verion: 'v1'
            api_url: 'https://api.spotify.com'
            auth_method: 'authentication method'

            * auth_method can be CLIENT_CREDENTIALS or AUTHORIZATION_CODE""")
        raise
