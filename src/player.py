# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def move(self, string):
        control_mapping = {
            "n":self.current_room.n_to,
            "e":self.current_room.e_to,
            "s":self.current_room.s_to,
            "w":self.current_room.w_to,
        }
        try:
            if control_mapping[string] == None:
                print('\nInvalid direction.')
            else:
                self.current_room = control_mapping[string]
        except:
            print('\nInvalid command.')

    def take_item(self, item_name):
        try:
            for item in self.current_room.items:
                if item_name == item.name:
                    self.inventory.append(item)
                    self.current_room.items.remove(item)
                    item.on_take()
        except:
            print(f"{item_name} was not found in the room.")

    def drop_item(self, item_name):
        try:
            for item in self.inventory:
                if item_name == item.name:
                    self.inventory.remove(item)
                    self.current_room.items.append(item)
                    item.on_drop()
        except:
            print(f"{item_name} was not found in your inventory.")

