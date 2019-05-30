# Write a class to hold player information, e.g. what room they are in
# currently.

from Item import LightSource

class Player:
    def __init__(self, name, current_room, items = []):
        self.name = name
        self.current_room = current_room
        self.items = items

    def take_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)
    
    def travel(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            player_light_source = [item for item in self.items if type(item) == LightSource]
            room_light_source = [item for item in self.current_room.items if type(item) == LightSource]
            if self.current_room.is_light or len(player_light_source) or len(room_light_source) > 0:
                self.current_room.__str__()
        else:
            print("\nYou cannot move in that direction.\n")
