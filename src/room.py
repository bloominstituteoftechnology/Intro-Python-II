# Implement a class to hold room information. This should have name and
# description attributes.

class Room: 
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def direction(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 's':
            return self.s_to
        elif direction == 'w':
            return self.w_to
        elif direction == 'e':
            return self.e_to
        else:
            return None
        def __repr__(self):
            return str(f'{self.name}')