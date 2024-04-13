import json
import requests


client_id = "__"
client_secret = "__"

endpoint = "https://api.foursquare.com/v3/places/search"

city = input("Введите город: ")
place = input("Введите заведение: ")
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "near": city,
    "query": place
}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI="
}

response = requests.get(endpoint, params=params, headers=headers)

if response.status_code == 200:
    print("Успешный запрос")
    data = json.loads(response.text)
    Values = data['results']
    for venue in Values:
        print('Название', venue['name'])
        print("Категория:")
        for index, catogory in enumerate(venue["categories"], start=1):
            print(f'{index}. {catogory["short_name"]}')
else:
    print('Error')
