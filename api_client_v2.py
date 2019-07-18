import requests, json

methods = {0: 'http://reqres.in', 1: '/api/users/2', 2: '/api/unknown/2', 3: '/api/unknown/23', 4: '/api/users?page=2'}


def ReqSend():
    return (json.dumps(request.json(), sort_keys=True, indent=4) + '\n')


def ReqStat():
    if request.status_code == 200:
        return '\nStatus: OK\nCode: ' + str(request.status_code)

    else:
        return '\nStatus: ERROR\nCode: ' + str(request.status_code)


def ReqUrl():
    return ('\nRequested URL: ' + request_url)


def ReqJs():
    return ('\nResponse:' + '\n' + ReqSend() + '\n')


while True:
    send = input('Enter method number or stop for exit: ')
    request_url = (methods[0] + methods[int(send)])
    request = requests.get(request_url)

    if int(send) in range(1, 5):
        print(ReqUrl(), ReqStat(), ReqJs())

    elif send == ('stop'):
        break

    else:
        print(
            '\n---------------------------------------------------\nERROR: enter number of method or type stop for exit\n---------------------------------------------------\n')
