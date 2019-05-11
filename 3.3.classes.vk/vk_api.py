from time import sleep

import requests


class vk_api:

    access_token = ''
    url = 'https://api.vk.com/method'
    client_id = ''
    version = 5.52
    user = {}
    # __login = False

    def __init__(self, access_token, client_id):

        self.access_token = access_token
        self.client_id = client_id


    def __request(self, method, params):

        result_api = requests.get(f'{self.url}{method}', params=params)

        data = 'Error'

        if result_api.status_code == 200:
            data = result_api.json()
        else:
            print('Что-то пошло не так ...')

        return data

    def auth(self):

        params = {
            'client_id': self.client_id,
            'v': self.version,
            'access_token': self.access_token
        }

        data = self.__request('/users.get', params)

        return data['response'][0]

    def friends(self):

        params = {
            'fields': 'firs_name,last_name',
            'user_id': self.user.get('id'),
            'v': self.version,
            'access_token': self.access_token
        }
        sleep(0.5)
        data = self.__request('/friends.get', params)
        friends_get = data['response']['items']

        return friends_get

    def relation(self, id_relate):

        params = {
            'source_uid': self.user.get('id'),
            'target_uid': id_relate,
            'v': self.version,
            'access_token': self.access_token
        }
        sleep(0.5)
        data = self.__request('/friends.getMutual', params)

        return data['response']

    def userinfo(self, userid):

        params = {
            'user_ids': userid,
            'v': self.version,
            'access_token': self.access_token
        }
        sleep(0.5)
        data = self.__request('/users.get', params)

        if len(data['response']) == 0:
            data = {}
        else:
            data = data['response'][0]

        return data




