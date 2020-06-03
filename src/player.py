from room import Room
from item import Item


# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    '''The player; holds current room'''
    def __init__(self, initial_room: Room):
        self.__current_room = initial_room
        self.items_list: list(Item) = []

    def enter_room(self, room: Room):
        '''Change player's current room to the one provided'''
        if room.can_enter(self):
            self.__current_room = room
        else:
            print("<The room is locked and you don't have the key.>")

    def take_item(self, item: Item):
        '''Adds item from current room to inventory;
        throws exception if room does not contain item'''
        assert self.current_room.items_list.__contains__(item)
        self.current_room.items_list.remove(item)
        self.items_list.append(item)
        item.on_take()

    def drop_item(self, item: Item):
        '''Drops item from inventory;
        throws exception if room does not contain item'''
        assert self.items_list.__contains__(item)
        self.items_list.remove(item)
        self.current_room.items_list.append(item)
        item.on_drop()

    @property
    def current_room(self):
        '''The room the player is currently in'''
        return self.__current_room

    @property
    def inventory(self):
        '''Comma-separated string of all item names'''
        if len(self.items_list) == 0:
            return "<empty>"
        return ', '.join([item.name for item in self.items_list])
