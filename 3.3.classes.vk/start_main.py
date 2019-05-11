from vk_api import *
from vk_user import *


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
                vk_item.add(ervk.userinfo(item_relation))
            vk_users.append(vk_item)

    else:
        print('В этот раз не прокатило ... :-(')

    for item in vk_users:
        print(item.first_name(), item.last_name())
        for item_relation in item.relations():
            print('\t', item_relation.get('first_name'), item_relation.get('last_name'))

if __name__ == '__main__':
    main()
