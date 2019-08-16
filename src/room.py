# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name=None, description=None, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f'room: {self.name}, description: {self.description}'


    def get_room(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

# test = Room("foyer", "kinda dusty", items =['hat','sword', 'sheild'])

# print(test.room_items())