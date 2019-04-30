
def get_cook_book():

    with open('recipes.txt', encoding='utf8') as book:
        cook_book = {}
        read_header = False
        read_qty = False
        tmp_recipe = ''
        for line in book:

            # чтение заголовка
            if not read_header:
                tmp_recipe = line.strip('\n')
                cook_book[tmp_recipe] = list()
                read_header = True
                tmp_list = []

            # чтение количества
            elif not read_qty:
                range_lines = int(line)
                for i in range(range_lines):
                    line_ingredient = book.readline()
                    get_list = line_ingredient.split('|')
                    cook_book[tmp_recipe].append(
                        {'ingridient_name': get_list[0], 'quantity': int(get_list[1]), 'measure': get_list[2].strip('\n')})
                book.readline()
                read_header = False
                read_qty = False
    return cook_book


def cook_selected(cooking, persons):
    prepare_list = dict()
    cook_book = get_cook_book()
    for dish in cooking:
        for dish_prepare in cook_book[dish]:
            if prepare_list.get(dish_prepare['ingridient_name']) is None:
                prepare_list[dish_prepare['ingridient_name']] = {'quantity': dish_prepare.get('quantity'),
                                                                 'measure': ' шт'}
            else:
                update_value = dish_prepare['quantity']
                current_value = prepare_list[dish_prepare['ingridient_name']].get('quantity')
                prepare_list[dish_prepare['ingridient_name']].update({'quantity': current_value + update_value})
    for item_prepare in prepare_list.keys():
        prepare_list[item_prepare].update({'quantity': prepare_list[item_prepare].get('quantity') * persons})

    print(prepare_list)



def main():

    add_cook = []
    cook_book = get_cook_book()
    while True:
        print('========= Меню ============')
        for menu_item in cook_book.keys():
            print(f'| {menu_item}')
        print('---------------------------')
        print('| 1-Приготовить | 0-Выход |')
        print('===========================')
        choice_menu = input('Выбор : ')

        if choice_menu == '0':
            break
        elif choice_menu == '1':
            persons = int(input('На сколько персон? -> '))
            cook_selected(add_cook, persons)
            add_cook = []
        else:
            if cook_book.get(choice_menu) == None:
                print('\nПункт меню отсутствует !\n')
            else:
                print(add_cook.append(choice_menu))

if __name__ == '__main__':
    main()