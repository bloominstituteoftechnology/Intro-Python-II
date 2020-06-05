# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
    def __str__(self):
        return f' {self.name}, {self.description}'

    def mapping(self, movement):
        
        if movement == 'up':
            return self.n_to
        
        elif movement == 'down':
            return self.s_to

        elif movement == 'left':
            return self.w_to
        
        elif movement == 'right':
            return self.e_to

        else:
            return None