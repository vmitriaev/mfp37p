import requests, json

class ReqRes():
    '''Запросы к reqres.in'''
    basic_url = ('http://reqres.in')

    def __init__(self, endpoint):
        '''Инициализация объекта класса ReqRes.'''
        self.endpoint = endpoint

    def sendRequestGet(self):
        '''Отправка GET запроса.'''
        return requests.get(self.basic_url + self.endpoint)

get_single_user = ReqRes('/api/users/2')

print(get_single_user.sendRequestGet())