# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.list = []

    def __str__(self):
        return f'{self.name} {self.current_room} {self.list}'

    def addItem(self, item):
        self.list.append(item)

    def removeItem(self, item):
        self.list.remove(item)

