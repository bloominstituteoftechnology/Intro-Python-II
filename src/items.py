# Class to hold item information
from abc import ABC, abstractmethod

class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    
    @abstractmethod
    def describe(self):
        pass


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        super().__init__(name, description, value)
        self.damage = damage
    def describe(self):
        print(f'''Item Name: {self.name}
        Item Description: {self.description}
        Item Value: {self.value} copper
        Item Damage: {self.damage}''')


class Book(Item):
    def  __init__(self, name, description, value, author):
        super().__init__(name, description, value)
        self.author = author
    def describe(self):
        print(f'''Item Name: {self.name}
        Item Description: {self.description}
        Item Value: {self.value} copper
        Item Author: {self.author}''')


class Basic(Item):
    def __init__(self, name, description, value, useful):
        super().__init__(name, description, value)
        self.useful = useful
    def describe(self):
        print(f'''Item Name: {self.name}
        Item Description: {self.description}
        Item Value: {self.value} copper
        Useful Item: {self.useful}''')

