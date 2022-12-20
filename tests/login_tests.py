import json

from json import dumps
from uuid import uuid4

import requests

from assertpy.assertpy import assert_that

#from config import BASE_URI
#from utils.print_helpers import pretty_print


## POST init
#url = "https://mhcdev.com/mobile/api/init"
payload = {}
headers = {}


response = requests.request("POST", url, headers=headers, data=payload)
jsonData = json.dumps(response.text)



print(jsonData)
print(type(jsonData))


print(response.text)




#Authorization = (response.text[0])
#csrf_token = (response.text[2])
#print(Authorization)
#print(csrf_token)
#authorization = ("Authorization", requests.payload)
#eval(authorization)
#print(authorization)
#csrfToken = str("CSRF", jsonData.CSRF)
#eval(csrfToken)
