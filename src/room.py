# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, is_light, items = [], n_to = None, s_to = None, e_to = None, w_to = None):
        self.name = name
        self.description = description
        self.is_light = is_light
        self.items = items

    def get_item(self, item):
        self.items.append(item)

    def lose_item(self, item):
        self.items.remove(item)

    def __str__(self):
        print(f"--------------------\n\n{self.name}\n\n\n{self.description}\n\n--------------------\n\n")

    def get_room_in_direction(self, direction):
        if direction in ("n", "s", "e", "w"):
            if direction == "n" and hasattr(self, 'n_to'):
                return self.n_to
            elif direction == "s" and hasattr(self, 's_to'):
                return self.s_to
            elif direction == "e" and hasattr(self, 'e_to'):
                return self.e_to
            elif direction == "w" and hasattr(self, 'w_to'):
                return self.w_to
            else:
                return None

class PuzzleRoom(Room):
    def __init__(self, name, description, player_puzzle_item, room_puzzle_item, is_light, items= []):
        super().__init__(name, description, is_light, items)
        self.player_puzzle_item = player_puzzle_item
        self.room_puzzle_item = room_puzzle_item

