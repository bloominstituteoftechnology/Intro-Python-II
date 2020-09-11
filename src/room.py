# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        # The room should also have n_to, s_to, e_to, and w_to attributes which point to the room in that respective direction.
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"{self.name}"

    def get_direction(self, direction):
        if direction == 'n':
            return self.n_to
        if direction == 's':
            return self.s_to
        if direction == 'e':
            return self.e_to
        if direction == 'w':
            return self.w_to
        else:
            return None

    def print_items(self):
        print("**************\n")
        ItemsInRoom = "This room currently holds: \n"
        for item in self.items:
            ItemsInRoom += "*" + str(item) + "\n"
        print(ItemsInRoom)
        print("*******************************************************************\n")

    def add_item(self, item):
        self.items.append(item)
        self.print_items()
    
    def take_item(self, item):
        if item in self.items:
            self.items.remove(item)
        self.print_items()

    
