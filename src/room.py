# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, list=[]):
        self.name = name
        self.description = description
        self.list = list
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None


    def addItem(self, item):
        return self.list.append(item)

    def removeItem(self, item):
        print(f'Items in: ' ,{self.list})