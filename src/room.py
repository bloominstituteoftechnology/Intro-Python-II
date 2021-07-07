# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to = None, s_to = None, e_to = None, w_to = None, items = []):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items
    
    def __str__(self):
        if len(self.items) > 0:
            return f"\nYou are currently in {self.name}.\n{self.description}\n\nYou spot some items in the distance\n\n{self.items[0]}\n{self.items[1]}"
        else:
            return f"\nYou are currently in {self.name}.\n{self.description}"
        
