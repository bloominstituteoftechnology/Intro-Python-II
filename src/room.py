# Implement a class to hold room information. This should have name and
# description attributes.

class Room(object):
    '''
    A Simple room object
    Params -
        name - a string with the name of the room
        description - a string with a description of what a player sees
    Attributes - default to None, user must define after instantiation
        n_to - references a different Room object to the north of this Room
        s_to - references a different Room object to the south of this Room
        e_to - references a different Room object to the east of this Room
        w_to - references a different Room object to the west of this Room
    '''

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return self.name + '\n' +self.description

class TreasureRoom(Room):
    '''
    An extension of the Room object, which contains items
    Params -
        name - a string with the name of the room
        description - a string with a description of what a player sees
        items - a list optionally containing items found in the room
    '''

    def __init__(self, name, description, items = []):
        self.items = items
        super(TreasureRoom, self).__init__(name, description)

    def pstring_items(self):
        '''
        Pretified string of all items
        '''
        return ', '.join([str(item) for item in self.items])
