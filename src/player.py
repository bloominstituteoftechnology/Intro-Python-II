# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    """
    Class for player object
    """

    # constructor with positional args and an empty list for items to be held
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    
    def __str__(self):
        return f'{self.current_room}'

    
    # # unused method for adding multiple items
    
    # def add_item(self, *args):
    #     for item in args:
    #         if item not in self.items:
    #             self.items.append(item)