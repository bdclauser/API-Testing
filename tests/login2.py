import requests
import json
from http import HTTPStatus

# trying different approach
import pytest
import responses

from json import dumps
from json import dump


## POST init
# @responses.activate
def init():
    """Queries the endpoint and returns an Authorization Key and a CSRF token"""


payload = {"key1": "value1", "key2": "value2", "key3": "value3"}
headers = {}

responseObject = requests.post(
    "https://mhcdev.com/mobile/api/init", headers=headers, data=payload
)

jsonData = responseObject.json()
print(jsonData)
print()
jsonStringData = dumps(jsonData)


Authorization = jsonData["AUTH"]
csrf_token = jsonData["CSRF"]
print(Authorization)
print()
print(csrf_token)


def login():
    

    payload = {"login_email": "brian.clauser@mhc.org", "login_password": "", "token": csrf_token }
    url = 'https:mhcdev.com/mobile/api/login'

    x = requests.post(url, data = payload, headers={'Content-Type': 'text/html; charset=UTF-8', 'Connection': 'keep-alive', 'Referrer-Policy': 'strict-origin', 'X-Content-Type-Options': 'nosniff', 'X-Frame-Options': 'SAVEORIGIN'}, cookies=jar)

    print(x.text)

    jar = requests.cookies.RequestsCookieJar()
    jar.set('tasty_cookie', 'yum', domain='mhcdev.com', path='/cookies')

    