# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    '''A room the player can enter'''

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__adjacent_rooms = {
            'n': None,
            's': None,
            'e': None,
            'w': None
        }

    def get_room_in_direction(self, direction):
        try:
            return self.__adjacent_rooms[direction]
        except KeyError:
            return None

    def __set_room_in_direction(self, direction, room):
        self.__adjacent_rooms[direction] = room

    n_to = property(
        lambda self: self.get_room_in_direction('n'),
        lambda self,value: self.__set_room_in_direction('n', value)
    )
    s_to = property(
        lambda self: self.get_room_in_direction('s'),
        lambda self,value: self.__set_room_in_direction('s', value)
    )
    e_to = property(
        lambda self: self.get_room_in_direction('e'),
        lambda self,value: self.__set_room_in_direction('e', value)
    )
    w_to = property(
        lambda self: self.get_room_in_direction('w'),
        lambda self,value: self.__set_room_in_direction('w', value)
    )
