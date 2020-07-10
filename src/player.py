# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f"PLAYER NAME: {self.name} \n{self.current_room}"

    def try_direction(self, action):
        attribute = action + "_to"

        # see if the current room has the attribute
        if hasattr(self.current_room, attribute):
            # `getattr` to move to the room
            self.current_room = getattr(self.current_room, attribute)

        else:
            print("You can't go that way!")

    def add_to_inventory(self, action_object):
        attribute = "item_" + action_object

        # see if current room has the attribute
        if hasattr(self.current_room, attribute):
            # add item to inventory
            item = getattr(self.current_room, attribute)
            self.inventory.append(item)

    def drop_from_inventory(self, action_object):
        # Ensure inventory isn't empty
        if len(self.inventory) > 0:
            # Loop into inventory
            for i in self.inventory:
                # grab item if object name string includes action_object
                if action_object in i.name:
                    item = i
                    self.inventory.remove(item)
        else:
            print("No items to drop!")

    def view_inventory(self):
        print("\nPLAYER INVENTORY: ")
        for i in self.inventory:
            i.print_name()
