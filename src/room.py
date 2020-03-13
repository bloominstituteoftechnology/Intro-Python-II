# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return_str = "\n--------\n"
        return_str += self.name
        return_str += "\n"
        return_str += self.description
        return_str += "\n"
        return_str += ', '.join(self.items)
        return_str += "\n--------\n"
        return return_str
    def get_exits_string(self):
        exits = []
        if(self.n_to is not None):
            exits.append("n")
        if(self.s_to is not None):
            exits.append("s")
        if(self.w_to is not None):
            exits.append("w")
        if(self.e_to is not None):
            exits.append("e")
        return exits
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        if self.items in item:
            self.items.remove(item)
            return True
        else:
            print(f"{item} is not in room.")
            return False