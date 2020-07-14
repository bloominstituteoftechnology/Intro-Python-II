# Write a class to hold player information, e.g. what room they are in
# currently.

class Player(object):
    """
    A simple player class
    Params - 
        name - a string containing the players name
    Attributes - Defaults to None, user must define after instantiating
        current_room - a reference to the current room the player is in
    """

    def __init__(self, name, items = []):
        self.name = name
        self.items = items
        self.current_room = None

    def pstring_items(self):
        '''
        Pretified string of all items
        '''
        return ', '.join([str(item) for item in self.items])

    def get_item(self, item_name):
        # TODO implement picking up an item
        self.current_room.items.find(item_name)
