# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.adjacent_rooms = {}

    def get_opposite(self, direction):
        if direction == "north":
            return "south"
        elif direction == "south":
            return "north"
        elif direction == "east":
            return "west"
        elif direction == "west":
            return "east"
        else:
            return None

    def add_addjacent_room(self, room, direction, reciprocal = True):

        self.adjacent_rooms[direction] = room
        if reciprocal:
            opposite_direction = self.get_opposite(direction)

            room.adjacent_rooms[opposite_direction] = self

    def adjacent_room_for(self, direction):
        if direction in self.adjacent_rooms:
            return self.adjacent_rooms[direction]
        else:
            print(f'\nCan\'t go {direction} from here.')
            return self

    def list_visible_items(self):
        print("\nLooking around you see:")
        if len(self.items) < 1:
            print("Nothing interesting...")
        else:
            for item in self.items:
                print(f'- {item}')

    def get_item_named(self, item_name):
        return next((item for item in self.items if item.name == item_name), None)

    def add_items(self, *items):
        for item in items:
            self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)