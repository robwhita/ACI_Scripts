'''Authenticates into the APIC and retrieves token.

Has the following function:

get_token'''

import json
import requests
from credentials import APIC_HOST, username, password


def get_token():

    '''Authenticates into the APIC and retrieves token.'''

    uri = APIC_HOST + '/api/aaaLogin.json'

    credentials = {
    "aaaUser": {
        "attributes": {
        "name": username,
        "pwd": password
        }
    }
    }

    authenticate = requests.post(uri , data=json.dumps(credentials), verify=False)
    return authenticate.cookies
    