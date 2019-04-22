documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "general", "number": "10006"}
      ]

for item in documents:
    try:
            print(item['name'])
    except KeyError:
        print('Поле Name отсутствует')