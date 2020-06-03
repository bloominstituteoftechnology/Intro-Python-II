# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.__name = str(name)
        self.description = str(description)
        self.items = []
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def get_name(self):
        return self.__name

    def set_name(self, n):
        self.__name = n

    def items_in_room(self):
        print(f"\n\tItems in the room: {len(self.items)}")
        for i, item in enumerate(self.items, 1):
            print(f"\t\t{i}.) {item.description}")

    def add_item(self, item):
        self.items.append(item)

    def pickup_item(self, i):
        if i - 1 < 0 or i - 1 > len(self.items): return print('Wrong input')
        return self.items.pop(i)

    name = property(get_name, set_name)
