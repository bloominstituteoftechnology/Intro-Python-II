# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, is_light, n_to = None, s_to = None, e_to = None, w_to = None, items = []):
        self.name = name
        self.description = description
        self.is_light = is_light
        self.n_to = n_to
        self.s_to = s_to
        self.w_to = w_to
        self.e_to = e_to
        self.items = items

    def get_item(self, item):
        self.items.append(item)

    def lose_item(self, item):
        self.items.remove(item)

class PuzzleRoom(Room):
    def __init__(self, name, description, player_puzzle_item, room_puzzle_item, is_light, n_to = None, s_to = None, e_to = None, w_to = None, items= []):
        super().__init__(name, description, is_light, n_to, s_to, e_to, w_to, items)
        self.player_puzzle_item = player_puzzle_item
        self.room_puzzle_item = room_puzzle_item

