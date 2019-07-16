import requests
import json

usr = requests.get('http://reqres.in/api/users/2')

print(json.dumps(usr.json(), sort_keys=True, indent=4))
