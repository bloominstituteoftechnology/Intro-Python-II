# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from lib import NameStorage
from item import Item

class Player(NameStorage):
    def __init__(self, name: str, room: Room = None, storage=[], items: list = []):
        super().__init__(name, storage=storage)
        self.items = items
        self.room = room
    
    def move_player(self, new_room: Room):
        self.room = new_room

    def __str__(self):
        return str(self.__dict__)

    def getRoom(self):
        return str(self.room)
    
    def on_take(self, item: Item):
        self.items.append(item)
        print(f'\nYou have picked up the {item.name}.')

    def on_drop(self, item: Item):
        self.items.remove(item)
        print(f'You have dropped the {item.name}.')

    def on_action(self, cmd, item: Item):
        if cmd == 'take':
            self.on_take(item)
        else:
            self.on_drop(item)

    def print_inventory(self):
        if len(self.items) > 0:
            print(f'Your inventory includes:')
            [print(n) for n in self.items]
        else:
            print(f'You have no items in your inventory.')
        

