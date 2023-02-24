from utils.local_config import MY_PASSWORD

import requests


def get_authorization_and_csrf(session):
    """This function gets authorization and a CSRF token from an API"""
    response_object = session.post("https://mhcdev.com/mobile/api/init", timeout=5.001)
    response_json = response_object.json()

    # Get the SESSIONID from cookies
    SESSIONID = next(c.value for c in response_object.cookies if c.name == "PHPSESSID")

    AUTHORIZATION = response_json.get("AUTH")
    csrf_token = response_json.get("CSRF")
    return SESSIONID, AUTHORIZATION, csrf_token


def login(session, SESSIONID, AUTHORIZATION, csrf_token):
    """This function logs in"""
    payload = {
        "login_email": "brian.clauser@mhc.org",
        "login_password": MY_PASSWORD,
        "token": csrf_token,
    }
    headers = {
        "Cookie": f"PHPSESSID={SESSIONID}",
        "Authorization": AUTHORIZATION,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    }
    response = session.post(
        "https://mhcdev.com/mobile/api/login",
        data=payload,
        headers=headers,
        timeout=5.001,
    )
    print(response.text)


def g2fa(session, AUTHORIZATION):
    """login requires g2fa, going to need a manual entry to variable"""
    url = "https://mhcdev.com/mobile/api/login-g2fa"
    payload = {"code": "209231"}
    files = []
    headers = {
        "Cookie": f"PHPSESSID={SESSIONID}",
        "Authorization": AUTHORIZATION,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Content-Type": "application/json",
    }
    response_object = session.post(url, headers=headers, data=payload, files=files)
    response_json = response_object.json()
    AUTHORIZATION = response_json.get("AUTH")
    csrf_token = response_json.get("CSRF")
    return AUTHORIZATION, csrf_token


# main code
if __name__ == "__main__":
    session = requests.Session()
    SESSIONID, AUTHORIZATION, csrf_token = get_authorization_and_csrf(session)
    login(session, SESSIONID, AUTHORIZATION, csrf_token)
