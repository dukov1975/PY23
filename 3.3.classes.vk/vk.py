from time import sleep
import requests


class Vk_api:

    def __init__(self, client_id):

        self.client_id = client_id
        self.url = 'https://api.vk.com/method'
        self.version = 5.52
        self.user = {}
        self.access_token = '0731d4ac34877e181ee8879d1821a362417d73511643e12c7105a38301a1e8a8671e7e60c723cb52a4e29'

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


class Vk_user:

    def __init__(self, json_result, vk_connect):
        self.user_json = json_result
        self.relation_users = []
        self.vk_api_connect = vk_connect
        relations = vk_connect.relation(self.user_json['id'])
        for item_relation in relations:
            self.relation_users.append(Vk_user_relation(vk_connect.userinfo(item_relation)))

    def __and__(self, other):
        return_list_mutal = []
        for relate in self.relation():
            for compare in other.relation():
                if relate == compare:
                    return_list_mutal.append(relate)
        return return_list_mutal

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

    def relation(self):
        return self.relation_users

    def __str__(self):
        return '{} {}'.format(self.user_json['first_name'], self.user_json['last_name'])


class Vk_user_relation(Vk_user):

    def __init__(self, json_result):
        self.user_json = json_result


def main():
    vk = Vk_api('6978871')

    owner = Vk_user(vk.auth(), vk)
    print(owner)
    vk_users = []

    if owner.id != '':
        print('Опознание друзей ...')
        for item_friend in vk.friends():
            vk_users.append(Vk_user(item_friend, vk))
        vk_users.append(owner)
    else:
        print('В этот раз не прокатило ... :-(')

    list_to_compare = vk_users

    for item in vk_users:
        for item_compare in list_to_compare:
            if item != item_compare:
                print(item, '<-*->', item_compare)
                mutal_user_list = item & item_compare
                for print_user_mutal in mutal_user_list:
                    print('\t', print_user_mutal)


if __name__ == '__main__':
    main()
