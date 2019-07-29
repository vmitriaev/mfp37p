import requests, json

endPoints = [['get', 'users?page=2'], ['get', 'users/2'], ['get', 'users/23'], ['get', 'unknown'], ['get', 'unknown/2'],
             ['get', 'unknown/23'], ['post', 'users'], ['put', 'users/2'], ['patch', 'users/2'], ['delete', 'users/2'],
             ['post', 'register'], ['post', 'register'], ['post', 'login'], ['post', 'login'], ['get', 'users?delay=3']]

postb = ['{"name":"morpheus","job":"leader"}', '{"email":"eve.holt@reqres.in","password":"pistol"}',
         '{"email":"sydney@fife"}', '{"email":"eve.holt@reqres.in","password":"cityslicka"}',
         '{"email":"peter@klaven"}']

basicUrl = ('https://reqres.in/api/')


def urlConstructor():
    '''Формирует окончательный endpoint реквеста'''
    url = endPoints[number - 1][1]
    return basicUrl + url


def methodConstructor():
    '''Получает метод запроса'''
    method = endPoints[number - 1][0]
    return method


def requestConstructor():
    '''Формирует и отправляет запрос'''
    if methodConstructor() == 'get':
        return requests.get(urlConstructor())

    elif methodConstructor() == 'post':
        if number == 7:
            return requests.post(urlConstructor(), data=(postb[0]))

        elif number == 11:
            return requests.post(urlConstructor(), data=postb[1])

        elif number == 12:
            return requests.post(urlConstructor(), data=postb[2])

        elif number == 13:
            return requests.post(urlConstructor(), data=postb[3])

        elif number == 14:
            return requests.post(urlConstructor(), data=postb[4])

        else:
            errMsg = ('ERROR: invalid request')
            l = '-' * len(errMsg)
            print('\n' + l + '\n' + errMsg + '\n' + l + '\n')

    elif methodConstructor() == 'put':
        return requests.put(urlConstructor(), data='{"name":"morpheus","job":"zion resident"}')

    elif methodConstructor() == 'patch':
        return requests.patch(urlConstructor(), data='{"name":"morpheus","job":"zion resident"}')

    elif methodConstructor() == 'delete':
        return requests.delete(urlConstructor())

    else:
        errMsg = ('ERROR: invalid method of request')
        l = '-' * len(errMsg)
        return '\n' + l + '\n' + errMsg + '\n' + l + '\n'


def responseCodeConstructor():
    '''Обрабатывает код ответа'''
    if requestConstructor().status_code in (200, 201):
        return '\nStatus: OK\nCode: ' + str(requestConstructor().status_code)

    elif requestConstructor().status_code in (404, 204, 400):
        return '\nStatus: ERROR\nCode: ' + str(requestConstructor().status_code)

    else:
        errMsg = ('ERROR: invalid status of response')
        l = '-' * len(errMsg)
        return '\n' + l + '\n' + errMsg + '\n' + l + '\n'


def responseJsonConstructor():
    '''Выдает форматированный json ответа'''
    return json.dumps(requestConstructor().json(), sort_keys=True, indent=4)


def requestViewer():
    '''Выводит значение запроса'''
    if str(requestConstructor().request) == '<PreparedRequest [GET]>':
        return '[GET]'

    elif str(requestConstructor().request) == '<PreparedRequest [POST]>':
        return '[POST]'

    elif str(requestConstructor().request) == '<PreparedRequest [PUT]>':
        return '[PUT]'

    elif str(requestConstructor().request) == '<PreparedRequest [PATCH]>':
        return '[PATCH]'

    elif str(requestConstructor().request) == '<PreparedRequest [DELETE]>':
        return '[DELETE]'

    else:
        errMsg = ('ERROR: invalid method of request')
        l = '-' * len(errMsg)
        return '\n' + l + '\n' + errMsg + '\n' + l + '\n'


while True:
    number = int(input('Choose request and type number here (for exit type 0): '))

    if number in range(1, 16, 1):
        print(requestViewer(), urlConstructor(), responseCodeConstructor(), '\n', 'Response: ', '\n',
              responseJsonConstructor())

    elif number == 0:
        break

    else:
        errMsg = ('ERROR: invalid number of request')
        l = '-' * len(errMsg)
        print('\n' + l + '\n' + errMsg + '\n' + l + '\n')
