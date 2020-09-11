# Implement a class to hold room information. This should have name and
# description attributes.
valid_directions = ('n','s','e','w')

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return '{self.name} {self.description}'.format(self=self)

    def show_directions(self):
        possible_directions = filter(lambda d: getattr(self, f"{d}_to") is not None, valid_directions)
        return ", ".join(list(map(to_upper, possible_directions)))

    def print_welcome(self):
        print(f'Welcome to {self.name}!')
        print(f'{self.description}')

    def show_items(self):
        if self.items.__len__() == 0:
            return "room has no items"
        else:
            return ", ".join(list(map(lambda it: it.name, self.items)))
