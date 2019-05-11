class vk_user:

    relation_users = []

    def __init__(self, json_result):
        self.user_json = json_result

    def id(self):
        return self.user_json['id']

    def first_name(self):
        return self.user_json['first_name']

    def last_name(self):
        return self.user_json['last_name']

    def add(self, relate_user):
        self.relation_users.append(relate_user)

    def relation(self):
        return self.relation.users
