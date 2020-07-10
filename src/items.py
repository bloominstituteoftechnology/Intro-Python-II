class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return f'{self.name}\n=====\n{self.description} Value: {self.value}\n'


class Food(Item):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(name='Food',
                         description=f'An edible value with {self.amount}',
                         value=self.amount)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return f'{self.name}\n=====\n{self.description}\n' \
               f'Value: {self.value}\nDamage: {self.damage}'


class Spear(Weapon):
    def __init__(self):
        super().__init__(name='Spear',
                         description='A sharp pointed stick, ',
                         value=0,
                         damage=5)


class Gun(Weapon):
    def __init__(self):
        super().__init__(name='Gun',
                         description='A shooting machine. ',
                         value=10,
                         damage=10)