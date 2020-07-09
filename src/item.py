# Code for the Item class

class Item():
    """
    This object represents an item in the game

    Attributes:
        name (str): the name of this item
    """

    def __init__(self, name):
        """ Initializes an Item object, takes the item name (str) """
        self.name = name

    def on_take(self):
        """ Called when this item is picked up by the player """
        print("You have picked up", self.name)
    
    def on_drop(self):
        """ Called when this item is dropped by the player """
        print("You have dropped", self.name)


class LightSource(Item):
    """
    A specialized item that provides light
    """
    def on_drop(self):
        print("It's not wise to drop your source of light!")
