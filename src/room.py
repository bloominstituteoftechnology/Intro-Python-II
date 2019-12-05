# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    ''' class for room'''
    def __init__(self, room, description):
        self.room = room 
        self.description = description
        
class Direction(Room):
    def __init__(self, n_to, s_to, e_to, w_to, room, description):
        super().__init__(room, description)
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
    
    def __str__(self):
        return f'{self.n_to} put you in the {self.room}'
        # return f'{self.s_to} put you in the {self.room}'
        # return f'{self.e_to} put you in the {self.room}'
        # return f'{self.w_to} put you in the {self.room}'