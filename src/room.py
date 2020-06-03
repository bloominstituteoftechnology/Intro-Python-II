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
        print(f"There are {self.items.count()} in this room:")
        for i, item in enumerate(self.items, 1):
            print(f"\t{i}.) {item}")

    name = property(get_name, set_name)
