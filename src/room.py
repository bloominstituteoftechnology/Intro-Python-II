# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, message):
        self.name = name
        self.message = message
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        '''
        This is a string method
        '''
        return f"{self.name}\n\n{self.message}"

