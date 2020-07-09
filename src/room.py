# Implement a class to hold room information. This should have name and
# description attributes.
# assigned name and desc as well as set up directional connections 
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None 
    def __str__(self):
            return f'{self.name}, {self.description}'