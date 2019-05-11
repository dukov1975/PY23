from time import sleep
import requests


class vk_api:

    def __init__(self, client_id):

        self.client_id = client_id
        self.url = 'https://api.vk.com/method'
        self.version = 5.52
        self.user = {}
        self.access_token = 'dde2217f5c5342e0a309e2d7f532529e78b63ea56427d595336adaa2d9040e92eabf86c6ac577bb65354b'

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

    def __init__(self, json_result, vk_connect):
        self.user_json = json_result
        self.relation_users = []
        self.vk_api_connect = vk_connect
        relations = vk_connect.relation(self.user_json['id'])
        for item_relation in relations:
            self.relation_users.append(vk_connect.userinfo(item_relation))

    def id(self):
        return self.user_json['id']

    def first_name(self):
        return self.user_json['first_name']

    def last_name(self):
        return self.user_json['last_name']

    def relation(self):
        return self.relation_users


def main():
    vk = vk_api('6978871')
    print('Опознование самого себя ...')
    owner = vk_user(vk.auth(), vk)
    vk_users = []

    if owner.id != '':
        print('Опознание друзей ...')
        for item_friend in vk.friends():
            # print(item_friend.get('id'), item_friend.get('first_name'), item_friend.get('last_name'))
            vk_users.append(vk_user(item_friend, vk))
        vk_users.append(owner)
    else:
        print('В этот раз не прокатило ... :-(')

    for item in vk_users:
        print(item.first_name(), item.last_name())
        for item_relation in item.relation():
            print('\t', item_relation.get('first_name'), item_relation.get('last_name'))


if __name__ == '__main__':
    main()
