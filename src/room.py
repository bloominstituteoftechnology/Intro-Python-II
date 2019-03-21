# Implement a class to hold room information. This should have name and
# description attributes.

#Rooms hold an items list

class Room:
    def _init_(self, name, description, items=None):
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
    def _repr_(self):
        return f"{self.name}\n\n {self.description}\n\n You see: {self.items}"
    def get_room_in_direction(self.direction):
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

        pass