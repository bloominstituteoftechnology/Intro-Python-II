from items import items

# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f"{self.name}, {self.description}, with these items:, {self.items}"

    def n_to(self):
        if isinstance(self, 'outside'):
            # change room to foyer
        elif isinstance(self, 'narrow'):
            # change room to treasure
        else:
            print("You cannot go this way")
    
    def s_to(self):
        if isinstance(self, 'foyer'):
            # change room to outside
        elif isinstance(self, "overlook"):
            # change overlook to foyer
        elif isinstance(self, "narrow"):
            # change overlook to treasure
        else:
            print("You cannot go this way")
    
    def w_to(self):
        if isinstance(self, "narrow"):
            # change room to foyer
        else:
            print("You cannot go this way")

    def e_to(self):
        if isinstance(self, "foyer"):
            # change room to narrow
        else:
            print("You cannot go this way")
    