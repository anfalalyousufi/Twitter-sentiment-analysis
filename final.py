import requests
import json
from requests_oauthlib import OAuth1


def authenticate(path):
    """
    Reads a json file at given path, and authenticates to Twitter using
    OAuth v1.

    Parameters
    ==========
    path : string
        Path to the credentials file. (See Notes.)

    Returns
    =======
    client : requests.session

    Notes
    =====
    The credentials file should be like this:

        {
            "CONSUMER_KEY" : "",
            "CONSUMER_SECRET" : "",
            "TOKEN_KEY" : "",
            "TOKEN_SECRET" : ""
        }
    """
    with open(path) as f:
        credentials = json.load(f)
    return _authenticate(credentials)


def _authenticate(credentials):
    try:
        oauth = OAuth1(client_key=credentials['CONSUMER_KEY'],
                       client_secret=credentials['CONSUMER_SECRET'],
                       resource_owner_key=credentials['TOKEN_KEY'],
                       resource_owner_secret=credentials['TOKEN_SECRET'],
                       signature_type='auth_header')
        client = requests.session()
        client.auth = oauth
        return client
    except (KeyError, TypeError):
        print('Error setting auth credentials.')
        raise