# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, description, direction = None):
        self.name = name
        self.description = description
        self.direction = direction
        # self.items = items
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None


    def __call__(self, direction):
        print(f"Room.__call__ called! direction={direction}")
        self.direction_method = {
            "n": self.n_to,
            "s": self.s_to,
            "w": self.w_to,
            "e": self.e_to
        }
        return self.direction_method[direction]

    def __str__(self):
        return f'{self.name}.\n{self.description}'
