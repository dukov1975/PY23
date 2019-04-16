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

    def __init__(self, name, weight):
        super().__init__(name, weight)

    @property
    def voice(self):
        return 'Кря-кря'

    @property
    def type_of(self):
        return 'Утка'
