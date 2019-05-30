import requests
import base64
from time import sleep


class Vk_api:

    def __init__(self):

        self.url = 'https://api.vk.com/method'
        self.version = 5.52
        self.user = ''
        self.access_token = ''
        self.respond_success = True
        with open('token') as token:
            coded_token = token.readline()
            self.access_token = base64.b64decode(coded_token).decode('utf-8')

    def __request(self, method, params):

        result_api = requests.get(f'{self.url}{method}', params=params)

        data = 'Error'

        if result_api.status_code == 200:
            data = result_api.json()
        else:
            print('Что-то пошло не так ...', result_api)

        return data

    def auth(self):

        params = {
            'v': self.version,
            'access_token': self.access_token
        }

        data = self.__request('/users.get', params)

        return data['response'][0]

    def friends(self):

        params = {
            'fields': 'firs_name,last_name',
            'user_id': self.user,
            'v': self.version,
            'access_token': self.access_token
        }

        data = self.__request('/friends.get', params)
        friends_get = data['response']['items']

        return friends_get

    def user_info(self, userid):

        params = {
            'user_ids': userid,
            'v': self.version,
            'access_token': self.access_token
        }

        data = self.__request('/users.get', params)
        try:
            data = data['response'][0]
            self.user = data['id']
        except KeyError:
            data = {}

        return data

    def groups(self, user_id):

        params = {
            'user_id': user_id,
            'v': self.version,
            'access_token': self.access_token
        }

        while self.respond_success:

            data = self.__request('/groups.get', params)
            try:
                groups_get = data['response']['items']
                self.respond_success = False
            except KeyError:
                # print(data)
                if data['error']['error_code'] == 6:
                    sleep(0.5)
                else:
                    groups_get = []
                    self.respond_success = False

        self.respond_success = True

        return groups_get

    def group_info(self, group_id):

        params = {
            'group_id': group_id,
            'fields': 'members_count',
            'v': self.version,
            'access_token': self.access_token
        }
        groups_get = {}
        while self.respond_success:
            data = self.__request('/groups.getById', params)
            # print('group_info', data)
            try:
                groups_get = data['response'][0]
                self.respond_success = False
            except KeyError:
                sleep(0.5)
                groups_get = {}

        self.respond_success = True

        return groups_get
