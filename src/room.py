# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None,items=[]):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items=items

def put_item(self,item_name):
        self.items = self.items.append(Item[item_name])

def take_item(self,item_name):
    self.items = self.items.remove(item_name)
        