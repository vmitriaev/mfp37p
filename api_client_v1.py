import requests
import json

usrlst = requests.get('http://reqres.in/api/users?page=2')

usrone = requests.get('http://reqres.in/api/users/2')

print(json.dumps(usrone.json(), sort_keys=True, indent=4))
