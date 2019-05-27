import requests
import json
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
            print('Что-то пошло не так ...')

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

        while self.respond_success:
            try:
                data = self.__request('/friends.get', params)
                friends_get = data['response']['items']
                self.respond_success = False
            except Exception:
                print('Ошибка в получении данных ...')
                sleep(0.5)
        self.respond_success = True

        return friends_get

    def user_info(self, userid):

        params = {
            'user_ids': userid,
            'v': self.version,
            'access_token': self.access_token
        }
        while self.respond_success:
            try:
                data = self.__request('/users.get', params)
                if len(data['response']) == 0:
                    data = {}
                else:
                    data = data['response'][0]
                    self.user = data['id']
            except Exception:
                    print('Ошибка в получении данных ...')
                    sleep(0.5)
        self.respond_success = True

        return data

    def groups(self, user_id):

        params = {
            'user_id': user_id,
            'v': self.version,
            'access_token': self.access_token
        }

        while self.respond_success:
            try:
                data = self.__request('/groups.get', params)
                try:
                    groups_get = data['response']['items']
                except Exception:
                    groups_get = []
            except Exception:
                print('Ошибка в получении данных ...')
                sleep(0.5)
        self.respond_success = True

        return groups_get

    def group_info(self, group_id):

        params = {
            'group_id': group_id,
            'fields': 'members_count',
            'v': self.version,
            'access_token': self.access_token
        }

        while self.respond_success:
            try:
                data = self.__request('/groups.getById', params)
                try:

                    groups_get = data['response'][0]

                except Exception:
                    groups_get = {}
            except Exception:
                print('Ошибка в получении данных ...')
                sleep(0.5)
            self.respond_success = True

        return groups_get


class Vk_user:

    def __init__(self, json_result, vk_connect):
        self.user_json = json_result
        self._friends = []
        self._groups = vk_connect.groups(self.id())
        print('Жертва :', self.first_name(), self.last_name())
        print('Группы жертвы кол-во:', len(self._groups))
        all_friends = vk_connect.friends()
        i = 0
        friend_count = len(all_friends)
        for friend in all_friends:
            print(f'\rПолучаем друзей с группами : {int(100.0 / friend_count * i)}%', end='')
            self._friends.append(Vk_friends(friend, vk_connect))
            i += 1

    def __ne__(self, other):
        return self.id() != other.id()

    def __eq__(self, other):
        return self.id() == other.id()

    def id(self):
        return self.user_json['id']

    def first_name(self):
        return self.user_json['first_name']

    def last_name(self):
        return self.user_json['last_name']

    def friends(self):
        return self._friends

    def groups(self):
        return self._groups

    def __str__(self):
        return '{} {}'.format(self.user_json['first_name'], self.user_json['last_name'])


class Vk_friends(Vk_user):

    def __init__(self, json_result, vk_connect):
        self.user_json = json_result
        self._groups = vk_connect.groups(self.user_json['id'])


def main():

    vkapi = Vk_api()

    try:
        while True:

            group_counters = {}
            user_id = input('Введите имя или ID жертвы:')
            print('Начат сбор информации ...')

            try:
                victim = Vk_user(vkapi.user_info(user_id), vkapi)
                for grp_id in victim.groups():
                    group_counters[grp_id] = 0
                print('\nРазбор и запись в формат JSON')
                for friend in victim.friends():
                    if len(friend.groups()) != 0:
                        for group_id in victim.groups():
                            group_counters[group_id] = group_counters[group_id] + friend.groups().count(group_id)

                to_json = []

                for group_json in group_counters:
                    if group_counters[group_json] == 0:
                        new_group = vkapi.group_info(group_json)
                        to_json.append(
                            dict(gid=group_json, name=new_group['name'], members_count=new_group['members_count']))

                with open('groups.json', mode='w', encoding='utf-8') as json_write:
                    json.dump(to_json, json_write, indent=4, ensure_ascii=False)

            except Exception:
                print('Наверно что-то ввели не так !!!')

    except KeyboardInterrupt:
        print('\r', 'Выход из программы')


if __name__ == '__main__':
    main()
