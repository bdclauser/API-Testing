import json
import requests
from assertpy.assertpy import assert_that

from json import dumps
from config import BASE_URI
from utils.print_helpers import pretty_print
from uuid import uuid4


## POST init
url = BASE_URI+"/init"
payload = {}
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

jsonData = json.parse(response.text)
authorization = ("Authorization", jsonData.AUTH)
csrfToken = ("CSRF", jsonData.CSRF)
