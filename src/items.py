# Class to hold item information

class Item:
    def __init__(self, ID, name, description, value):
        self.ID = ID
        self.name = name
        self.description = description
        self.value = value


class Weapon(Item):
    def __init__(self, name description value, damage):
        super().__init__(name, description, value)
        self.damage = damage


class Book(Item):
    def  __init__(self, name, description, value, author):
        super().__init__(name, description, value)
        self.author = author


class Basic(Item):
    def __init__(self, name, description, value, useful):
        super().__init__(name, description, value)
        self.useful = useful

# dagger = Weapon('Stabby', 'A short dagger.', 5, 2)
# sword = Weapon('Slash', 'A large sword.', 12, 4)
# needle = Weapon('Pokey', 'A long, needle-like sword. (stick them with the pointy end)', 25, 9)
# candle = Basic('Candle', 'Just a candle', 1, False)
# shoes = Basic('Shoes', 'Pair of Jordans. What are those doing here?', 20, True)
# book = Book('Book', 'An old book, most of the pages are faded', 3, 'Unknown')
# great_book = Book('Cryptonomicon', 'A fantastic book, seriously read it', 20, 'Neal Stephenson')
