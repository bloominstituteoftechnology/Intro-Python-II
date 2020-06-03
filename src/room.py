from __future__ import annotations
from item import Item

# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    '''A room the player can enter'''
    def __init__(self, name: str, description: str):
        self.name = name
        self.__description = description
        self.__adjacent_rooms = {
            'n': None,
            's': None,
            'e': None,
            'w': None
        }
        self.items_list = []

    def can_enter(self, _) -> bool:
        return True

    # the next line should not throw a warning, but it does for me...
    def get_room_in_direction(self, direction: str) -> Room:
        '''Returns room (or `None`) in provided cardinal direction string'''
        try:
            return self.__adjacent_rooms[direction]
        except KeyError:
            return None

    def __set_room_in_direction(self, direction: str, room):
        self.__adjacent_rooms[direction] = room

    @property
    def item_names(self):
        '''A formatted string containing the comma-separated names of all
        items in room'''
        return ', '.join([item.name for item in self.items_list])

    @property
    def description(self):
        '''A physical description of the room and its contents'''
        if len(self.items_list) > 0:
            return f"{self.__description}\nItems visible: {self.item_names}"
        return self.__description

    n_to = property(
        lambda self: self.get_room_in_direction('n'),
        lambda self, value: self.__set_room_in_direction('n', value))
    s_to = property(
        lambda self: self.get_room_in_direction('s'),
        lambda self, value: self.__set_room_in_direction('s', value))
    e_to = property(
        lambda self: self.get_room_in_direction('e'),
        lambda self, value: self.__set_room_in_direction('e', value))
    w_to = property(
        lambda self: self.get_room_in_direction('w'),
        lambda self, value: self.__set_room_in_direction('w', value))


class KeyedRoom(Room):
    '''A room that requires a key to enter'''
    def __init__(self, name: str, description: str, key: Item):
        self.required_key = key
        super().__init__(name, description)

    def can_enter(self, p) -> bool:
        return self.required_key in p.items_list
