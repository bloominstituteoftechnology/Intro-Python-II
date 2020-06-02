# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    '''The player; holds current room'''
    def __init__(self, initial_room):
        self.current_room = initial_room
        self.items_list = []

    def enter_room(self, room):
        '''Change player's current room to the one provided'''
        self.current_room = room

    def take_item(self, item):
        '''Adds item from current room to inventory;
        throws exception if room does not contain item'''
        assert self.current_room.items_list.__contains__(item)
        self.current_room.items_list.remove(item)
        self.items_list.append(item)

    def drop_item(self, item):
        '''Drops item from inventory;
        throws exception if room does not contain item'''
        assert self.items_list.__contains__(item)
        self.items_list.remove(item)
        self.current_room.items_list.append(item)
