# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    """
    Class for the Room object
    """

    # object constructor with position args and an empty list attribute for holding items
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    
    def __str__(self):
        return f'{self.name}'

    
    # # unused method to unpack an iterable
    
    # def add_item(self, *args):
    #     for item in args:
    #         if item not in self.items:
    #             self.items.append(item)


    # declaring empyty attributes to be filled later
    n_to = None
    s_to = None
    e_to = None
    w_to = None