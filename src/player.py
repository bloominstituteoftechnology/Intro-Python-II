# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, room):
        self.name = name 
        self.room = room
        self.inventory = []

    def addItem(self, item):
        self.inventory.append(item)

    def removeItem(self, item):
      index = self.inventory.index(item)
      self.inventory.pop(index)



