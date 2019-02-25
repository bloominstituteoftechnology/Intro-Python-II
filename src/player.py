# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self,name, currentRoom, items):
        self.name = name
        self.currentRoom = currentRoom,
        self.items = items
    def __str__(self):
        return f'player name: {self.name} current room: {self.currentRoom}'
    def addItem(item):
        self.items.append(item)
    def listItems():
        for item in self.items:
            print(item)
