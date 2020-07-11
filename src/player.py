# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room):
        self.room = room
        self.items = []


    
    def grab_item(self, item):
        self.room.remove_item(item)
        self.items.append(item)
        return f"You picked up {item.name}"
    
    def drop_item(self, item):
        self.room.append(item)
        self.items.remove(item)
    
    def __repr__(self):
        return "{room: "+self.room+"}"
