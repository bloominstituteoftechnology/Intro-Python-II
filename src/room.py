# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    # Room contains: name, description, items_in_room. Methods: add_item
    def __init__(self, name, description, items_in_room, n_to, s_to, e_to, w_to):
        self.name = name
        self.description = description
        self.items_in_room = []
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def __str__(self):
        return f' Current room: {self.room} \n Description: {self.description} \n Items In Room: {self.items_in_room} \n '


# room = Room()
