# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name="", desc="", items=[]):
        self.name = name
        self.desc = desc
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return "Room name: {}, desc: {}".format(self.name, self.desc)

    def printAllItems(self):
        items = ""
        length = len(self.items)
        if length > 0:
            for (index, item) in enumerate(self.items):
                items += item.name
                if index != length - 1:
                    items += ", "
            print(f'This is all items in this room: {items}')
        else:
            print(f"There isn't any item in this room")