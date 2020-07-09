# Implement a class to hold room information. This should have name and
# description attributes.

import textwrap
from item import LightSource

def print_wrapped(message, width=50):
    """ Prints a message using the textwrap module """
    wrapper = textwrap.TextWrapper(width) 
    message = wrapper.wrap(message) 
    for line in message: 
        print(line)


class Room():
    """
    The Room class, handles the room name and description, and keeps track of
    what other rooms can be moved to from here.

    Attributes:
        name (str): the name of this room
        description (str): the description of this room
        n_to (Room): the room to the north
        s_to (Room): the room to the south
        e_to (Room): the room to the east
        w_to (Room): the room to the west
        items (list): a list of Items in this room
        is_light (bool): True if the room is light enough to see
        locks (list): a list of directions with locked doors
    """

    def __init__(self, name, description, is_light=True, locks=[]):
        """ Initializes a room, takes a name and description """
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
        self.is_light = is_light
        self.locks = locks
    
    def add_item(self, item):
        """ adds an item to this room """
        self.items.append(item)
    
    def take_item(self, item_name):
        """ removes an item from this room and returns it """
        for i in range(len(self.items)):
            if self.items[i].name == item_name:
                return self.items.pop(i)
        
        # No item with that name found
        return None
    
    def print_description(self, has_light):
        """
        Prints the room description to the console

        has_light (bool): pass in True if the player has a light
        """

        print_wrapped(self.name)

        # Print description if we can see
        if self.is_light or has_light:
            print_wrapped(self.description)
        else:
            print("It's pitch black in here!")

        if self.is_light or has_light:
            # Show all items in the room
            for item in self.items:
                print("You see a", item.name)
        else:
            # Only show light sources
            for item in self.items:
                if type(item) == LightSource:
                    print("You see a", item.name)
