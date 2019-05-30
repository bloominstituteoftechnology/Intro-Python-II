# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, is_light, items = []):
        self.name = name
        self.description = description
        self.is_light = is_light
        n_to = None
        s_to = None
        e_to = None
        w_to = None
        self.items = items

    def get_item(self, item):
        self.items.append(item)

    def lose_item(self, item):
        self.items.remove(item)

    def __str__(self):
        print(f"--------------------/n/n{self.name}/n/n/n{self.description}/n/n--------------------/n/n")

    def get_room_in_direction(self, direction):
        if direction in ("n", "s", "e", "w"):
            if direction == "n":
                return self.n_to
            if direction == "s":
                return self.s_to
            if direction == "e":
                return self.e_to
            if direction == "w":
                return self.w_to
            else:
                print("Invalid command. Please enter a valid command.")

class PuzzleRoom(Room):
    def __init__(self, name, description, player_puzzle_item, room_puzzle_item, is_light, items= []):
        super().__init__(name, description, is_light, items)
        self.player_puzzle_item = player_puzzle_item
        self.room_puzzle_item = room_puzzle_item

