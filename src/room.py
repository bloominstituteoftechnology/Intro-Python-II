# Implement a class to hold room information. This should have name and
# description attributes.
from lib import Description
from item import Item

class Room(Description):
    """ This is a Room. """
    def __init__(self, name, description, storage=[], items: list = []):
        super().__init__(name, description, storage=storage)
        self.items = items
        self.n_to: Room = None
        self.s_to: Room = None
        self.e_to: Room = None
        self.w_to: Room = None

    def __str__(self):
        return str(self.__dict__)

    def on_take(self, item: Item):
        self.items.remove(item)

    def on_drop(self, item: Item):
        self.items.append(item)

    def on_action(self, cmd, item: Item):
        if cmd == 'take':
            self.on_take(item)
        else:
            self.on_drop(item)
