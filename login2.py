
import requests
from local_config import MY_PASSWORD




def get_authorization_and_csrf(session):
    """
    Get the authorization and csrf token from the API.

    The function makes a POST request to the API endpoint https://mhcdev.com/mobile/api/init using the session object.
    It raises an exception if the request fails (i.e., status code is not 200 OK).

    The function returns the following:

    SESSIONID: a string in the format "PHPSESSID=<value>"
    AUTHORIZATION: the value of the "AUTH" key from the JSON response
    csrf_token: the value of the "CSRF" key from the JSON response
    Parameters:
    session (requests.Session): a session object to make the API request with

    Returns:
    Tuple[str, str, str]: SESSIONID, AUTHORIZATION, and csrf_token respectively

    Raises:
    Exception: if the API request fails"""
    response_object = session.post(
        "https://mhcdev.com/mobile/api/init",
        timeout=5.001,
    )
    status_code = response_object.status_code
    status_ok = response_object.ok
    if not status_ok:
        raise Exception(f"Request failed with status code {status_code}")
    for c in response_object.cookies:
        if c.name == "PHPSESSID":
            SESSIONID = f"{c.name}={c.value}"

    json_data = response_object.json()
    AUTHORIZATION = json_data.get("AUTH")
    csrf_token = json_data.get("CSRF")
    return SESSIONID, AUTHORIZATION, csrf_token


def login(session, SESSIONID, AUTHORIZAION, csrf_token):
    """
    This function logs in to the given URL with the provided credentials and headers.

    Parameters:
    session (requests.Session): An instance of requests.Session to use for the request.
    SESSIONID (str): The session ID to be used in the request headers.
    AUTHORIZAION (str): The authorization token to be used in the request headers.
    csrf_token (str): The CSRF token to be included in the request payload.

    Returns:
    None
    """
    payload = {
        "login_email": "brian.clauser@mhc.org",
        "login_password": MY_PASSWORD,
        "tokent": csrf_token,
    }
    headers = {
        "Cookie": SESSIONID,
        "Authorization": AUTHORIZAION,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    }
    resp = session.post(
        "https://mhcdev.com/mobile/api/login",
        data=payload,
        headers=headers,
        timeout=5001,
    )
    print(resp.text)


# main code
session = requests.Session()
SESSIONID, AUTHORIZATION, csrf_token = get_authorization_and_csrf(session)
login(session, SESSIONID, AUTHORIZATION, csrf_token)
