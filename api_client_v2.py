import requests, json

methods = {1: '/api/users/2', 2: '/api/unknown/2', 3: '/api/unknown/23', 4: '/api/users?page=2'}
basic_url = ('http://reqres.in')


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


#def GoUrl():
#    return str(basic_url + methods[int(send)])


while True:
    send = str(input('Enter method number or stop for exit: '))

    if send in ('1', '2', '3', '4'):
        request_url = (basic_url + methods[int(send)])
        request = requests.get(request_url)
        print(ReqUrl(), ReqStat(), ReqJs())

    elif send in ('stop', 'exit', '0'):
        break

    else:
        print(
            '\n---------------------------------------------------\nERROR: enter number of method or type stop for exit\n---------------------------------------------------\n')
