"""This is my example for now... to do..."""
import json
import requests


def get_init_response():
    """Performs a POST request to the API endpoint and returns the response."""
    url = "https://mhcdev.com/mobile/api/init"
    headers = {}
    response = requests.post(url, headers=headers, timeout=5.001)
    try:
        response_json = response.json()
    except json.JSONDecodeError:
        print("Failed to decode the response as JSON.")
        response_json = {}
    csrf_token = response_json.get("CSRF")
    authorization = response_json.get("AUTH")
    return csrf_token, authorization
