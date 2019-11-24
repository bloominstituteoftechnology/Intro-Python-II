class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        output = f'You have found {self.name}. \n'
        output += f'{self.description} \n'
        return output

    def inspect(self):
        output = f'{self.name} Attributes: \n'
        return output

class Weapon(Item):
    def __init__(self, name, description, attk_pwr):
        super().__init__(name, description)
        self.attk_pwr = attk_pwr
        self.slot = 'right_hand'

    def inspect(self):
        output = super().inspect() + '\n'
        output += f'Attack Power: {self.attk_pwr} \n'
        return output

class Shield(Item):
    def __init__(self, name, description, defense):
        super().__init__(name, description)
        self.defense = defense
        self.slot = 'left_hand'

    def inspect(self):
        output = super().inspect() + '\n'
        output += f'Defense Power: {self.defense} \n'
        return output

class Armor(Item):
    def __init__(self, name, description, defense, slot):
        super().__init__(name, description)
        self.defense = defense
        self.slot = slot

    def inspect(self):
        output = super().inspect() + '\n'
        output += f'Defense Power: {self.defense} \n'
        return output

class HealthPotion(Item):
    def __init__(self, name, description, restores):
        super().__init__(name, description)
        self.restores = restores

    def inspect(self):
        output = super().inspect() + '\n'
        output += f'Potency: {self.restores}hp \n'
        return output