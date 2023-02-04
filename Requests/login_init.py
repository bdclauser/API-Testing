import requests
import logging
import os
from tests import local_config

MY_PASSWORD = local_config.MY_PASSWORD


# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

url = "https://mhcdev.com/mobile/api/init"

payload = {
    "login_email": "brian.clauser@mhc.org",
    "login_password": MY_PASSWORD,
    "token": "YdHDyVvTPFNPFWhGgjz54Rqkq7TsVS9mPHghr8pr1v0dV2zb7pB292fNpHKS2Hjs",
}
files = []

# Define headers in a separate dictionary
headers = {}

try:
    # Make the POST request
    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    # Log the request and response details
    logging.debug(f"Request Headers: {response.request.headers}")
    logging.debug(f"Request Body: {response.request.body}")
    logging.debug(f"Response Headers: {response.headers}")
    logging.debug(f"Response Status Code: {response.status_code}")
    logging.debug(f"Response Content: {response.text}")

    # Raise an exception if the status code is not 200
    response.raise_for_status()
except Exception as e:
    logging.error(f"Request failed: {e}")
