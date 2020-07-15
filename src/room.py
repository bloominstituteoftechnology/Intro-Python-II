# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __str__(self):
        if self.name.startswith('Outside'):
            val = f'You are {self.name}.'
        else:
            val = f'You are in the {self.name}.'
        val += f'\n{self.description}'
        return val
