class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return f'{self.name}\n=====\n{self.description} Value: {self.value}\n'

    def on_take(self):
        print(f'You have picked up {self.name}!\n')

    def on_drop(self):
        print(f'You have dropped {self.name}!\n')


class Gold(Item):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(name='Gold',
                         description=f'A round coin with {self.amount}'
                                     f' stamped on the front.',
                         value=self.amount)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return f'{self.name}\n=====\n{self.description}\n' \
               f'Value: {self.value}\nDamage: {self.damage}'


class Rock(Weapon):
    def __init__(self):
        super().__init__(name='Rock',
                         description='A fist-sized rock, '
                                     'suitable for bludgeoning.',
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name='Dagger',
                         description='A small dagger with some rust. '
                                     'Somewhat more dangerous than a rock.',
                         value=10,
                         damage=10)
