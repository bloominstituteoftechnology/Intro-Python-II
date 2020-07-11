# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, items_in_room = []):
        self.name = name
        self.items_in_room = items_in_room

    # method for setting some of the attributes
    # for the class
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

    