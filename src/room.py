# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    # constructor
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items
    # adding a default representation
    def __repr__(self):
        return(f'Location: {self.name}. You see that {self.description}.') # need to add a bit to this that changes first letter of description to lowercase
