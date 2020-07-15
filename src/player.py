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
        '''
        Takes an item from the current room and adds it to players item list
        Only acts on the first item found.
        Params -
            item_name - name of the item desired by the player
        Returns - True if successful, False if failed
        '''
        # give me a list of items that match the item name. Should be only 
        # unless user is creating duplicates
        item_refs = [item for item in self.current_room.items if str(item).lower() == item_name.lower()]

        # remove only the first item found
        if len(item_refs) > 0:
            self.items.append(item_refs[0])
            self.current_room.items.remove(item_refs[0])
            return True
        else:
            return False

    def drop_item(self, item_name):
        '''
        Takes an item from the players item list and adds it to the current
        room's item list. Only acts on the first item found.
        Params -
            item_name - a string containing the name of the item to be dropped
        Returns - True if dropped, False if failed to drop
        '''

        item_refs = [item for item in self.items if str(item).lower() == item_name.lower()]

        if len(item_refs) > 0:
            self.current_room.items.append(item_refs[0])
            self.items.remove(item_refs[0])
            return True
        else:
            return False

