# Implement a class to hold room information. This should have name and
# description attributes.
##remeber this ***** to add items to super
class Room: 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def show_room_items(self):
        if len(self.items) == 0:
            print("The room is empty of items")
        else:
            print(f'You can see a: ')
            for item in self.items:
                print(item.name)