# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self,name, currentRoom, items):
        self.name = name
        self.currentRoom = currentRoom,
        self.items = items
    def __str__(self):
        return f'player name: {self.name} current room: {self.currentRoom}'
    def addItem(self,item):
        self.items.append(item)
        item.on_take();

    def inventory(self):
        for item in self.items:
            print(item)
    def drop(self,item):
        print('in drop')
        print(item)
        item.on_drop()
        self.items.remove(item)
        self.listItems()
