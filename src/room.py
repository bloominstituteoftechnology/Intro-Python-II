# Implement a class to hold room information. This should have title and
# description attributes.
from player import Player

class Room:
    """
    room class
    """
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = []
        if len(self.items) > 0:
            for item in self.items:
                self.items.append(item)
        else:
            self.items = items

    def __str__(self):
        return f' {self.name}\n\n{self.description}'

    def room_inventory(self):
        if self.items == []:
            print('no items here')
        elif type(self.items) is list :
            for item in self.items:
                print(f'there is a {item.name} ')
        else:
            print(f'here there is a {self.items.name} ')

    def take_item(self, item):
        self.items.remove(item)
        Player.add_item(item)