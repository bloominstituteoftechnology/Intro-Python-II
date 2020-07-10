# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Item

class Player:
    def __init__(self, name, current_room):
        super().__init__()
        self.name = name
        self.current_room = current_room
        self.items = []
        
    def __str__(self):
        return f'Name: {self.name}, Current Room: {self.current_room}'
    
    def move_room(self, direction):
        if getattr(self.current_room, f'{direction}_to'):
            self.current_room = getattr(self.current_room, f'{direction}_to')
    
    def print_items(self):
        if len(self.items) > 0:
            print('Your current items:\n')
            for i in self.items:
                print(f'{i.name} - {i.description}')
        else:
            print('You have no items - explore the map to find some and add them to your collection!')

    def search_items(self, item):
        for i in self.items:
            if i.name.lower() == item:
                return i
            else:   
                return None

    def add_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)