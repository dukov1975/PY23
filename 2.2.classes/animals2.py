class Voice:

    __type_voices = {'Cow': 'Му-му', 'Goose': 'Га-Га', 'Ship': 'Бе-бе', 'Chicken': 'Ко-ко', 'Goat': 'Ме-ме', 'Duck': 'Кря-кря'}

    @property
    def voice(self):
        return self.__type_voices.get(type(self).__name__)

class Production(Voice):

    __type_production = {'Подоить': ['Cow', 'Goat'], 'Собрать яйца': ['Goose', 'Chicken', 'Duck'], 'Подстрич': ['Ship']}

    @property
    def production(self):
        production_name = ''
        for product_item in self.__type_production.keys():
            for product_values in self.__type_production[product_item]:
                if product_values == type(self).__name__:
                    production_name = product_item
        return production_name

    def __init__(self):
        super().__init__()

class Animal(Production):

    __type_animals = {'Cow': 'Корова', 'Goose': 'Гусь', 'Ship': 'Овца', 'Chicken': 'Курица', 'Goat': 'Козел', 'Duck': 'Утка'}

    def __init__(self, name, weigth):
        super().__init__()
        self.animal_name = name
        self.animal_weigth = weigth

    @property
    def type_of(self):
        return self.__type_animals.get(type(self).__name__)

    @property
    def to_feed(self):
        return 'Покормить'

class Cow(Animal):
    pass
class Goose(Animal):
    pass
class Ship(Animal):
    pass
class Chicken(Animal):
    pass
class Goat(Animal):
    pass
class Duck(Animal):
    pass

animals = [Cow('Манька', 320),
           Goose('Серый', 7),
           Goose('Белый', 8),
           Ship('Барашек', 30),
           Ship('Кудрявый', 35),
           Chicken('Ко-Ко', 2),
           Chicken('Кукареку', 3.2),
           Goat('Рог', 26),
           Goat('Копыто', 29),
           Duck('Кряква', 9),
           ]

total_weigth = 0
max_weigth = Cow('', 0)
for animal_item in animals:
    total_weigth += animal_item.animal_weigth
    print('Тип:{} Имя:{} Вес:{}кг Действие:{} Итого:{} Голос:{}'.format(
                                    animal_item.type_of, animal_item.animal_name, animal_item.animal_weigth,
                                    animal_item.to_feed, animal_item.production, animal_item.voice))
    if animal_item.animal_weigth > max_weigth.animal_weigth:
        max_weigth = animal_item

print('\nВсего кг:', total_weigth)
print('\nСамое тяжелое животное Тип:', max_weigth.type_of, 'Имя:', max_weigth.animal_name, 'Вес:', max_weigth.animal_weigth)



