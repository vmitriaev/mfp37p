import requests, json


class ReqRes():
    '''Содержит методы обращения к reqres.in'''

    def __init__(self, endpoint):
        '''Инициализация объекта класса ReqRes'''
        self.endpoint = endpoint
        self.basicUrl = ('https://reqres.in/api/')

    def requestGet(self):
        '''Формирует url и отправляет GET запрос'''
        final_url = self.basicUrl + self.endpoint
        sendGet = requests.get(final_url)
        return sendGet

    def requestPost(self):
        '''Формирует url и отправляет POST запрос'''

    def requestPut(self):
        '''Формирует url и отправляет PUT запрос'''

    def requestPatch(self):
        '''Формирует url и отправляет PATCH запрос'''

    def requestDelete(self):
        '''Формирует url и отправляет DELETE запрос'''

    def endPoint(self):
        '''Формирует окончательный url запроса'''


request1 = ReqRes('users/2')

print(request1.requestGet())
