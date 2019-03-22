# Implement a class to hold room information. This should have name and
# description attributes.

#Rooms hold an items list

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        if items is None:
            self.items = []
        else:
            self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __repr__(self):
        room_string = f"{self.name}\n\n"
        room_string += f"    {self.description}\n\n"
        room_string += f"You can move: {self.get_exits()}\n"
        if len(self.items) > 0:
            room_string += f"You see: {self.get_items_string()}"
        return room_string
    def get_items_string(self):
        return ', '.join([str(i) for i in self.items])
    def get_exits(self):
        exits = []
        if self.n_to is not None:
            exits.append('n')
        if self.s_to is not None:
            exits.append('s')
        if self.e_to is not None:
            exits.append('e')
        if self.w_to is not None:
            exits.append('w')
        return ", ".join(exits)
    def get_room_in_direction(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None
    def find_item_by_string(self, item_name):
        """
        Look through self.items for an item that matches the name
        """
        pass