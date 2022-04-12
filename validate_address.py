import requests
import json
import os

API_KEY = os.environ['API_KEY']
API_URL = os.environ['API_URL']


def validate_address(address):
    url = f"{API_URL}/validation"

    payload = json.dumps(address)
    headers = {
      'Ocp-Apim-Subscription-Key': f"{API_KEY}",
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


if __name__ == "__main__":
    test_address = {
      "firstname": "Markus Stahl",
      "street": "Am Anger 33",
      "town": "33332 Gutersloh"
    }

    result = validate_address(test_address)
    print(json.dumps(result, indent=4, sort_keys=True))
