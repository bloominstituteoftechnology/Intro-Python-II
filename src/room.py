# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    '''
     base class for rooms
    '''
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
