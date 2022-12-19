import json

from json import dumps
from uuid import uuid4

import requests

from assertpy.assertpy import assert_that

from utils.config import BASE_URI
from utils.print_helpers import pretty_print


## POST init
url = BASE_URI + "/init"
payload = {}
headers = {}


response = requests.request("POST", url, headers=headers, data=payload)
response_text = response.json()
pretty_print(response_text)

print(response.text)

jsonData = json.parse(response.text)
authorization = ("Authorization", jsonData.AUTH)
csrfToken = ("CSRF", jsonData.CSRF)
