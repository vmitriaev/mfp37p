# try to use requests library

import requests
import json

baseurl = "https://reqres.in/"
list_users = "api/users?page=2"
single_user = "api/users/2"

choose = input("Please, choose method:\n1. list_users\n2. single_user\nmethod:")

if choose == "list_users":

    req = requests.get(str(baseurl) + str(list_users))
    print(req.url)
    print(req.status_code)
    print(req.text)

elif choose == "1":

    req = requests.get(str(baseurl) + str(list_users))
    print(req.url)
    print(req.status_code)
    print(req.text)

elif choose == "1.":

    req = requests.get(str(baseurl) + str(list_users))
    print(req.url)
    print(req.status_code)
    print(req.text)

elif choose == "single_user":

    req = requests.get(str(baseurl) + str(single_user))
    print(req.url)
    print(req.status_code)
    print(req.text)

elif choose == "2":

    req = requests.get(str(baseurl) + str(single_user))
    print(req.url)
    print(req.status_code)
    print(req.text)

elif choose == "2.":

    req = requests.get(str(baseurl) + str(single_user))
    print(req.url)
    print(req.status_code)
    print(req.text)

else:
    print("Didn't read LOL")
