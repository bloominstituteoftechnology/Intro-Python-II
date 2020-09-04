# Implement a class to hold room information. This should have name and
# description attributes.
# from item import Item
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items_list = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return (self.items_list)

    def add_item(self, item):
        self.items_list.append(item)

    def remove_item(self, item):
        self.items_list.remove(item)


    
