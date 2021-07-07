# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item
class Player:
    def __init__(self, room):
        self.room = room
        self.items = []
        

    def __str__(self):
        return f'Player room={self.room}, items={self.items}'

    def show_items(self):
        for i in self.items:
            print(i.name)

    def get_item(self, new_item):
        self.items.append(new_item)

    def drop_item(self, item):
         for i in self.items:
            if i.name == item:
                self.items.remove(i)





