import requests
import json

url = "http://openlibrary.org/search.json"

subject = 'Artifical intelligence'

params = {
    "subject": subject,
    "limit": 1
}

response = requests.get(url, params=params)
if response.status_code == 200:
    print("Done")
else:
    print("faile", response.status_code)

print(response.text)