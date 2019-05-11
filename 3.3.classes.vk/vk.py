from time import sleep
import requests


class vk_api:
    access_token = ''
    url = 'https://api.vk.com/method'
    client_id = ''
    version = 5.52
    user = {}

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


class vk_user:

    def __init__(self, json_result):
        self.user_json = json_result
        self.relation_users = []

    def id(self):
        return self.user_json['id']

    def first_name(self):
        return self.user_json['first_name']

    def last_name(self):
        return self.user_json['last_name']

    def add(self, relate_user):
        self.relation_users.append(relate_user)

    def relation(self):
        return self.relation_users


def main():
    vk = vk_api('39ff0bb9c949cbcc08808c48a4eeae91adb4f50803bd7bbaab6e2975173541e59235492b5d2009a0a5436', '6978871')
    owner = vk_user(vk.auth())
    vk_users = []

    if owner.id != '':
        friends = vk.friends()
        for item_friend in friends:
            print(item_friend.get('id'), item_friend.get('first_name'), item_friend.get('last_name'))
            vk_item = vk_user(item_friend)
            relations = vk.relation(item_friend.get('id'))
            for item_relation in relations:
                vk_item.add(vk.userinfo(item_relation))
            vk_users.append(vk_item)

    else:
        print('В этот раз не прокатило ... :-(')

    for item in vk_users:
        print(item.first_name(), item.last_name())
        for item_relation in item.relation():
            print('\t', item_relation.get('first_name'), item_relation.get('last_name'))


if __name__ == '__main__':
    main()
