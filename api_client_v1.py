import requests
import json


def SendReq():
    url = ('http://reqres.in/')

    meth1 = ('api/users/2')

    meth2 = ('api/unknown/2')

    while True:
        if send == str(1):
            request = requests.get(url + meth1)
            return print(json.dumps(request.json(), sort_keys=True, indent=4))

        elif send == str(2):
            request = requests.get(url + meth2)
            return print(json.dumps(request.json(), sort_keys=True, indent=4))

        else:
            print('WAT')
            return


send = input('Enter method number (1/2): ')
while True:
    if send == str(1):
        print(SendReq())
        continue

    elif send == str(2):
        print(SendReq())
        continue

    elif send == ('exit'):
        break

    else:
        print('TAW')

# while True:
# if send == str(1):
# request = requests.get(url + meth1)
# print(json.dumps(request.json(), sort_keys=True, indent=4))
# continue

# elif send == str(2):
# request = requests.get(url + meth2)
# print(json.dumps(request.json(), sort_keys=True, indent=4))

# elif send == ('exit'):
# break

# else:
# print('WAT')
