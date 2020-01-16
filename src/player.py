# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        self.items = items
        
    def move_to_room(self, new_room):
        if new_room:
            self.current_room = new_room
            
    def pick_up_item(self, item):
        self.items.append(item)