class Animal:

    def __init__(self, name, weight):
        self.animal_name = name
        self.animal_weight = int(weight)

    @property
    def to_feed(self):
        return 'Покормить'

class Milk:

    @property
    def product(self):
        return 'Подоить'

class Trim:

    @property
    def product(self):
        return 'Подстрич'

class Egg:

    @property
    def product(self):
         return 'Собрать яйца'


class Cow(Animal, Milk):

    @property
    def voice(self):
        return 'Му-му'

    @property
    def type_of(self):
        return 'Корова'

class Goose(Animal, Egg):

    @property
    def voice(self):
        return 'Га-Га'

    @property
    def type_of(self):
        return 'Гусь'

class Ship(Animal, Trim):

    @property
    def voice(self):
        return 'Бе-бе'

    @property
    def type_of(self):
        return 'Овца'

class Chicken(Animal, Egg):

    @property
    def voice(self):
        return 'Ко-ко'

    @property
    def type_of(self):
        return 'Курица'


class Goat(Animal, Milk):

    @property
    def voice(self):
        return 'Ме-ме'

    @property
    def type_of(self):
        return 'Коза'

class Duck(Animal, Egg):

    @property
    def voice(self):
        return 'Кря-кря'

    @property
    def type_of(self):
        return 'Утка'

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
    total_weigth += animal_item.animal_weight
    print('Тип:', animal_item.type_of, ', Имя:', animal_item.animal_name,
          ', Вес:', animal_item.animal_weight, 'кг, Действие:', animal_item.to_feed,
          ', Итого:', animal_item.product, ', Голос:', animal_item.voice, sep='')
    if  animal_item.animal_weight > max_weigth.animal_weight:
        max_weigth = animal_item

print('\nВсего кг:', total_weigth)
print('\nСамое тяжелое животное Тип:', max_weigth.type_of, 'Имя:', max_weigth.animal_name, 'Вес:', max_weigth.animal_weight)