import json
from vk_api import Vk_api
from vk_friends import Vk_user


def main():
    vk_api = Vk_api()

    try:
        while True:

            group_counters = {}
            user_id = input('Введите имя или ID жертвы:')
            print('Начат сбор информации ...')
            victim = Vk_user(vk_api.user_info(user_id), vk_api)
            if len(victim.friends()) > 0:
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
                        new_group = vk_api.group_info(group_json)
                        to_json.append(
                            dict(name=new_group['name'], gid=group_json, members_count=new_group['members_count']))

                with open('groups.json', mode='w', encoding='utf-8') as json_write:
                    json.dump(to_json, json_write, indent=4, ensure_ascii=False)
            else:
                print('Что-то пошло не так ...')

    except KeyboardInterrupt:
        print('\r', 'Выход из программы')


if __name__ == '__main__':
    main()
