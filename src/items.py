# Class to hold item information

class Item:
    def __init__(self, ID, name='', description='', value=0):
        self.ID = ID
        self.name = name
        self.description = description
        self.value = value


class Weapon(Item):
    def __init__(self, name='', description='', value=0, damage=0):
        super().__init__(name=name, description=description, value=value)
        self.damage = damage


class Book(Item):
    def  __init__(self, name='', description='', value=0, author=''):
        super().__init__(name=name, description=description, value=value)
        self.author = author


class Basic(Item):
    def __init__(self, name='', description='', value=0, useful=True):
        super().__init__(name=name, description=description, value=value)
        self.useful = useful

dagger = Weapon('Stabby', 'A short dagger.', 5, 2)
sword = Weapon('Slash', 'A large sword.', 12, 4)
needle = Weapon('Pokey', 'A long, needle-like sword. (stick them with the pointy end)', 25, 9)
candle = Basic('Candle', 'Just a candle', 1, False)
shoes = Basic('Shoes', 'Pair of Jordans. What are those doing here?', 20, True)
book = Book('Book', 'An old book, most of the pages are faded', 3, 'Unknown')
great_book = Book('Cryptonomicon', 'A fantastic book, seriously read it', 20, 'Neal Stephenson')
