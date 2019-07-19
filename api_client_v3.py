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
        if str(self.method).lower() == str('get').lower():
            return json.dumps(self.requestGet().json(), sort_keys=True, indent=4)

        elif str(self.method).lower() == str('post').lower():
            return json.dumps(self.requestPost().json(), sort_keys=True, indent=4)

        elif str(self.method).lower() == str('put').lower():
            return json.dumps(self.requestPut().json(), sort_keys=True, indent=4)

        elif str(self.method).lower() == str('patch').lower():
            return json.dumps(self.requestPatch().json(), sort_keys=True, indent=4)

        elif str(self.method).lower() == str('delete').lower():
            return json.dumps(self.requestDelete().json(), sort_keys=True, indent=4)

        else:
            return 'Отсутствует метод запроса!'


request1 = ReqRes('get', 'users/2')

request2 = ReqRes('get', 'unknown/2')

print(request2.getFormattedJsonFromRequest())
