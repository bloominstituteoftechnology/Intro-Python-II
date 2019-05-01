# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    '''
     base class for rooms
    '''
    def __init__(self, name, desc, items = []):
        self.name = name
        self.desc = desc
        self.items = items

    def __repr__(self):
        return (f'{self.name}. {self.desc} {self.items}')