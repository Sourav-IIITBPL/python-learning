# requests is a third-party library that allows you to send HTTP requests using Python.
#  It is not included in the standard library, so you need to install it using pip before you can use it.

import requests
import sys
import json

response = requests.get("https://api.github.com")
print(json.dumps(response.json(), indent=4))  # returns the response in json format
print(response.status_code)  # 200 means OK, 404 means Not Found,