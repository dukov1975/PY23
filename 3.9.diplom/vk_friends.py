class Vk_user:

    def __init__(self, json_result, vk_connect):
        self._friends = []
        self._groups = []
        if len(json_result) > 0:
            self.user_json = json_result
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
