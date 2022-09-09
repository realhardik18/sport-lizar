import requests
import json
from creds import PANTRY_ID

url = f"https://getpantry.cloud/apiv1/pantry/{PANTRY_ID}/basket/cricket data"


def get_pantry():
    payload = ""
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


def update_pantry(item):
    data = get_pantry()
    data['webhooks'].append(item)
    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    requests.request("POST", url, headers=headers, data=payload)


# print(get_pantry())
