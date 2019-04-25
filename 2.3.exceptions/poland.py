class NoDigit(Exception):
    pass


class WrongArgument(Exception):
    pass


str_poland = input('Введите строку нотации: ')
str_list = str_poland.split(sep=' ')

try:

    action = str_list[0]

    result = 0

    if len(str_list) != 3:
        raise WrongArgument('')

    # тут был явный косяк, на скорую руку
    assert (action in ['+', '-', '/', '*']), 'NotFoundAction'

    # демонстрация знания в двух экзеплярах
    # Пример 1
    assert (str_list[1].isdigit()), 'NotDigit'

    # Пример 2, естественно в в реальном проекте все будет унифицировано и под одним знаменателем
    if not str_list[2].isdigit():
        raise NoDigit('')

    var1 = int(str_list[1])
    var2 = int(str_list[2])

    if action == '/':
        result = var1 / var2
    elif action == '*':
        result = var1 * var2
    elif action == '+':
        result = var1 + var2
    elif action == '-':
        result = var1 - var2
    print('Результат:', var1, action, var2, '=', result)
except WrongArgument:
    print('Неверное количество аргументов')
except NoDigit:
    print('Второй аргумент не число')
except ValueError:
    print('Неправильный тип данных')
except ZeroDivisionError:
    print('Деление на ноль')
    # так же в реальной жизни писать не буду, демонстрация знания предмета во всех направлениях
except Exception as e:
    if e.args[0] == 'NotFoundAction':
        print('Отсутствует операция над числами')
    elif e.args[0] == 'NotDigit':
        print('Первый аргумент не число')
    else:
        print(e)
finally:
    print('Конец')
