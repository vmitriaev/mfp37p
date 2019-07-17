import requests
import json

basic_url = ('http://reqres.in/')

meth1 = ('api/users/2')

meth2 = ('api/unknown/2')

meth3 = ('api/unknown/23')


def ReqStat():
    if request.status_code == 200:
        return ('\nStatus: OK\nCode: ' + str(request.status_code))

    else:
        return ('\nStatus: ERROR\nCode: ' + str(request.status_code))


def ReqUrl():
    return ('\nRequested URL: ' + request.url)


def ReqJs():
    return ('\nResponse:' + '\n' + json.dumps(request.json(), sort_keys=True, indent=4) + '\n')


while True:
    send = input('Enter method number (1/2/3): ')

    if send == str(1):
        request = requests.get(basic_url + meth1)
        print(ReqUrl(), ReqStat(), ReqJs())

    elif send == str(2):
        request = requests.get(basic_url + meth2)
        print(ReqUrl(), ReqStat(), ReqJs())

    elif send == str(3):
        request = requests.get(basic_url + meth3)
        print(ReqUrl(), ReqStat(), ReqJs())

    elif send == ('exit'):
        break

    else:
        print('1 or 2, please!')
