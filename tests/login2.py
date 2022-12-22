"""needed imports"""
import requests
import json
from config import MY_PASSWORD
from json import dumps

# import json
# from http import HTTPStatus
# from json import dump


"""This gets the authorization token and the csrf token"""
payload = {}
headers = {}
response_object = requests.request(
    "POST",
    "https://mhcdev.com/mobile/api/init",
    headers=headers,
    data=payload,
    timeout=5.001,
)
status_code = response_object.status_code
status_ok = response_object.ok

print(f"\n!!!!!!!!!! The status code of POST is {status_code} !!!!!!!!!!")
print(f"!!!!!!!!!! The response is {status_ok} !!!!!!!!!!\n")

for c in response_object.cookies:
    print(c.name + "==>>", c.value)

SESSIONID = (c.name) + "=" + (c.value)

jsonData = response_object.json()
data = json.dumps(jsonData, indent=1)
print(data)
# print(jsonData)
print("|================================================================|")
AUTHORIZATION = jsonData.get("AUTH")
print("Authorization:" + AUTHORIZATION)
print("||==============================================================||\n")
csrf_token = jsonData.get("CSRF")
print("CSRF:" + csrf_token)
print("||==============================================================||\n")


"""what's up doc"""
payload2 = {
    "login_email": "brian.clauser@mhc.org",
    "login_password": MY_PASSWORD,
    "token": csrf_token,
}

resp = requests.request(
    "POST",
    "https://mhcdev.com/mobile/api/login",
    data=payload2,
    headers={"Cookie": SESSIONID, "Authorization": AUTHORIZATION, "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"},
    timeout=5.001,
)

print(resp.text)
# print("If true Continue")


# """G2FA"""
# # code = input("Enter your 6-digit code: ")
# # code = int(code)

# payload3 = {"code": 215592}
# g2faResponse = requests.request(
#     "POST",
#     "https://mhcdev.com/mobile/api/login-g2fa",
#     headers={"Authorization": AUTHORIZATION, "Cookie": SESSIONID},
#     data=payload3,
#     files=[],
#     timeout=5.001,
# )
# print(g2faResponse.text)
