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
            if self.current_room.is_light or len(player_light_source) > 0 or len(room_light_source) > 0:
                self.current_room.__str__()
                if len(self.current_room.items) > 0:
                    for item in self.current_room.items:
                        print(f"You see a {item.name}.\n")
            else:
                print("It's pitch black!")
        else:
            print("\nYou cannot move in that direction.\n")

    def look(self):
        player_light_source = [item for item in self.items if type(item) == LightSource]
        room_light_source = [item for item in self.current_room.items if type(item) == LightSource]
        if self.current_room.is_light or len(player_light_source) > 0 or len(room_light_source) > 0:
            self.current_room.__str__()
            if len(self.current_room.items) > 0:
                for item in self.current_room.items:
                    print(f"You see a {item.name}.\n")
        else:
            print("You can't see a thing in this darkness!")

    def get_item(self, item_name):
        probable_item = self.current_room.has_item(item_name)
        if probable_item is not None:
            self.items.append(probable_item)
            self.current_room.items.remove(probable_item)
            probable_item.on_take()
        else:
            print("\nWhy are you trying to pick up something that isn't there? Are you okay?\n")

    def drop_item(self, item_name):
        probable_item = self.current_room.has_item(item_name)
        if probable_item is not None:
            self.items.remove(probable_item)
            self.current_room.items.append(probable_item)
            probable_item.on_drop()
        else:
            print("\nWhy are you trying to drop up something that you don't have? Are you okay?\n")

    def look_item(self, item_name):
        probable_item = self.current_room.has_item(item_name)
        if probable_item is not None:
            print(probable_item.description)
        else:
            print("\nYou don't need to look at that.\n")

