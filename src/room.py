# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name="", desc="", items=[], n_to=Room(), s_to=Room(), e_to=Room(), w_to=Room()):
        self.name = name
        self.desc = desc
        self.items = items
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def __str__(self):
        return "Room name: {}, desc: {}".format(self.name, self.desc)