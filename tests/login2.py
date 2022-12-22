"""needed imports"""
import requests
from config import my_password

# import json
# from http import HTTPStatus
# from json import dumps
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

for c in response_object.cookies:
    print(c.name + "==>>", c.value)
global sessionID
sessionID = (c.name) + "=" + (c.value)
print(sessionID)
print("00000000000000000000000000000000000000000000000000000000")
jsonData = response_object.json()
print(jsonData)
print("|================================================================|")
global authorization
authorization = jsonData.get("AUTH")
global csrf_token
csrf_token = jsonData.get("CSRF")
print("Authorization:" + authorization)
print("||==============================================================||")
print("CSRF:" + csrf_token)
print("||==============================================================||")


# def login():
#     payload = {
#         "login_email": "brian.clauser@mhc.org",
#         "login_password": my_password,
#         "token": csrf_token,
#     }

#     x = requests.request(
#         "POST",
#         "https:mhcdev.com/mobile/api/login",
#         data=payload,
#         headers={"Cookie": sessionID, "Authorization": authorization},
#     )

#     print(x.text)


# def g2fa():
#     code = input("Enter your 6-digit code: ")
#     code = int(code)

#     url = "https://mhcdev.com/mobile/api/login-g2fa"
#     payload = {"code": code}
#     files = []
#     headers = {"Authorization": authorization, "Cookie": sessionID}
#     g2faResponse = requests.request(
#         "POST", url, headers=headers, data=payload, files=files
#     )
#     print(g2faResponse.text)
