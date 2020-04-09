# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room, name='player1', items=None):
        self.name = name
        self.room = room
        self.items = [] if items is None else items

    def get_location(self):
        return self.room

    def set_location(self, room):
        self.room = room

    def take_item(self, item):
        self.items.append(item)
    
    def drop_item(self, item):
        self.items.remove(item)

    @property
    def inventory(self):
        return self.items