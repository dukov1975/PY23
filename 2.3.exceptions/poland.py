class NoDigit(Exception):
    pass


class WrongArgument(Exception):
    pass


str_poland = input('Введите строку нотации: ')
str_list = str_poland.split(sep=' ')

try:

    action = str_list[0]

    result = 0

    assert (action in '+-/*'), 'NotFoundAction'

    assert (str_list[1].isdigit()), 'NotDigit'

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
except Exception as e:
    if e.args[0] == 'NotFoundAction':
        print('Отсутствует операция над числами')
    elif e.args[0] == 'NotDigit':
        print('Первый аргумент не число')
    else:
        print(e)
finally:
    print('Конец')
