import requests, json


class ReqRes():
    '''Содержит методы обращения к reqres.in'''

    def __init__(self, method, endpoint):
        '''Инициализация объекта класса ReqRes'''
        self.method = method
        self.endpoint = endpoint
        self.basicUrl = ('https://reqres.in/api/')

    def requestGet(self):
        '''Отправляет GET запрос'''
        sendGet = requests.get(self.fullUrl())
        return sendGet

    def requestPost(self):
        '''Отправляет POST запрос'''

    def requestPut(self):
        '''Отправляет PUT запрос'''

    def requestPatch(self):
        '''Отправляет PATCH запрос'''

    def requestDelete(self):
        '''Отправляет DELETE запрос'''

    def fullUrl(self):
        '''Формирует окончательный url для запроса'''
        finalUrl = self.basicUrl + self.endpoint
        return finalUrl

    def getFormattedJsonFromRequest(self):
        '''Выводит форматированный JSON ответа сервиса.'''

        errorMessage = 'ERROR: REQUEST METHOD MISSING OR INCORRECT'
        lines = '-' * len(errorMessage)

        if str(self.method).lower() == 'get':
            return '\nResponse:\n' + json.dumps(self.requestGet().json(), sort_keys=True, indent=4)

        elif str(self.method).lower() == 'post':
            return '\nResponse:\n' + json.dumps(self.requestPost().json(), sort_keys=True, indent=4)

        elif str(self.method).lower() == 'put':
            return '\nResponse:\n' + json.dumps(self.requestPut().json(), sort_keys=True, indent=4)

        elif str(self.method).lower() == 'patch':
            return '\nResponse:\n' + json.dumps(self.requestPatch().json(), sort_keys=True, indent=4)

        elif str(self.method).lower() == 'delete':
            return '\nResponse:\n' + json.dumps(self.requestDelete().json(), sort_keys=True, indent=4)

        else:
            return '\n' + lines + '\nERROR: REQUEST METHOD MISSING OR INCORRECT\n' + lines

    def requestStatus(self):
        '''Вывод статуса запроса.'''
        if str(self.method).lower() == 'get':

            if self.requestGet().status_code == 200:
                return '\nStatus: OK\nCode: ' + str(self.requestGet().status_code)

            else:
                return '\nStatus: ERROR\nCode: ' + str(self.requestGet().status_code)

    def finalResponseOutput(self):
        '''Формирование окончательного ответа: вывод статуса, кода ответа и тела'''


request1 = ReqRes('get', 'users/2')

request2 = ReqRes('GET', 'unknown/2')

print(request2.requestStatus(), request2.getFormattedJsonFromRequest())
