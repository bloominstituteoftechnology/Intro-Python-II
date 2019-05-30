# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, at_room):
        self.at_room = at_room
        self.items_held = []

    def relocate (self, new_room):
        self.at_room = new_room
    
    def obtain_item (self, item):
        self.items_held.append(item)
    
    def drop_item (self, item):
        self.items_held.remove(item)

