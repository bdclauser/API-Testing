import requests
import json
from http import HTTPStatus

# trying different approach
import pytest
import responses

from json import dumps
from json import dump


## POST init
@responses.activate
def init():
    """Queries the endpoint and returns an Authorization Key and a CSRF token"""


payload = {"key1": "value1", "key2": "value2", "key3": "value3"}
headers = {}

responseObject = requests.post(
    "https://mhcdev.com/mobile/api/init", headers=headers, data=payload
)

jsonData = responseObject.json()

jsonStringData = dumps(jsonData)
Authorization = jsonData['AUTH']
print(Authorization)
#print(jsonStringData)
print()
print(type(jsonStringData))