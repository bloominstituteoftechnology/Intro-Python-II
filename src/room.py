# Implement a class to hold room information. This should have name and
# description attributes.
# Could've use the built in hasattr and getattr and setattr...
# I already typed the code soooooooooooooo... yeah.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
    def add_item(self, item):
        self.items.append(item)
    def __str__(self):
        return f'{self.name}'
    def get_n_to(self):
        return self.n_to
    def get_e_to(self):
        return self.e_to
    def get_s_to(self):
        return self.s_to
    def get_w_to(self):
        return self.w_to
    def get_inventory(self):
        if self.items.count > 0:
            for item in self.items:
                print(item.name)
        else:
            print("There is nothing in here.")