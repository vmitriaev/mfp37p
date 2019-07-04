# try to use requests library

import requests

r = requests.get('https://reqres.in/api/users/2')
r.text

print(r)
print(r.text)
print(r.encoding)
print(r.headers)