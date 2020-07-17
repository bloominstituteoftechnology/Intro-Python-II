# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    
    def __init__(self, name, description, dark_description=None, items_in_room = [], is_light=False, animal_monster=None):
        self.name = name
        self.description = description
        self.dark_description = dark_description
        self.items_in_room = items_in_room
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.is_light = is_light
        self.animal_monster = animal_monster


    # method for setting some of the attributes
    # for the class
    # This method is not used because the locations are set in the 
    # adv.py file.

    def set_next_to_attr(self, n_to, s_to, e_to, w_to):
        """
        used to set the attributes of what rooms are next to this room
        """
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    
    
    
    def list_items_in_room(self):
        return self.items_in_room

    def add_item(self, newItem):
        self.items_in_room.append(newItem)

    # function that will return the linked rooms in the 
    # order n , s, e, w
    # returns 0 if not linked in the direction and 1 if 
    # linked
    def return_room_links(self):
        theList = []
        if self.n_to == None:
            theList.append(0)
        else:
            theList.append(1)
        if self.s_to == None:
            theList.append(0)
        else:
            theList.append(1)
        if self.e_to == None:
            theList.append(0)
        else:
            theList.append(1)
        if self.w_to == None:
            theList.append(0)
        else:
            theList.append(1)
        return theList