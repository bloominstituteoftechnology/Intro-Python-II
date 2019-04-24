# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items
        self.adjacent_rooms = {}

    def add_addjacent_room(self, room, direction):
        if direction == "north":
            opposite_direction = "south"
        elif direction == "south":
            opposite_direction = "north"
        elif direction == "east":
            opposite_direction = "west"
        elif direction == "west":
            opposite_direction = "east"
        self.adjacent_rooms[direction] = room
        room.adjacent_rooms[opposite_direction] = self

    def adjacent_room_for(self, direction):
        if direction in self.adjacent_rooms:
            return self.adjacent_rooms[direction]
        else:
            print(f'\nCan\'t go {direction} from here.')
            return self

    def list_visible_items(self):
        print("\nLooking around you see:")
        if len(self.items) < 0:
            print("nothing...")
        else:
            for item in self.items:
                print(f'- a {item}')