# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
class Room:
    def __init__(self, name, description):
        """
        ! requires
            Class must be construvted with the name of room, and the description
            
        
        @params:
            name: room name
            description: describes room
            n/s/e/w_to: indictates direction that can a pklayer can morve to 
            iems: list of Item objects fir room
        
        """
        self.name = name
        self.description = description
        self.n_to: Room = None
        self.s_to: Room = None
        self.e_to: Room = None
        self.w_to: Room = None
        self.items = []

    def __repr__(self):
        return f"{self.name}: {self.description}"
    
    def took(self, item):
        self.items.remove(item)
        
    def added(self, item):
        self.items.append(item)