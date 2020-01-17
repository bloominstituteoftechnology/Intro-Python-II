# Write a class to hold player information, e.g. what room they are in
# currently.
import item
from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        
    def travel(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
        else:
            print("Can't move in that direction.")
            
    def pick_up_item(self, item):
        print(f"Picked up {item.name}")
        self.items.append(item)
        
    def drop_item(self, item):
        print(f"Dropped {item.name}")
        for i in self.items:
            if item.name == i.name:
                self.items.remove(i)
    
    def get_items(self):
        return f"Items {', '.join(self.items)}"
    
    