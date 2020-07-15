# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

direction_names = {
    'n': 'North',
    's': 'South',
    'e': 'East',
    'w': 'West'
    }

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        num_items = len(self.inventory)

        if len(num_items) > 0:
            s = "\n    "
            item_descriptions = s + s.join(str(item) for item in self.inventory)
        else:
            item_descriptions = "none"
        
        return f"""Player:
            Name: {self.name}
            Current room: {self.current_room.name}
            Items: {item_descriptions}
        """

    def try_direction(self, cmd):
        attribute = cmd + '_to'
        if hasattr(self.current_room, attribute):
            self.current_room = getattr(self.current_room, attribute)
            self.print_location_status()
        else:
            print(f"\nYou cannot move {direction_names[cmd]} from here. Please try another direction.\n")
    
    def print_location_status(self):
        print(f'\nYou are now in room: {self.current_room.name}\n')
        print(f"{self.current_room.description}\n")

        num_items = len(self.current_room.items)

        if num_items > 0:
            s = "\n    "
            item_descriptions = s + s.join(str(item) for item in self.current_room.items)
            item_plural = "item" if num_items == 1 else "items"
            print(f"This room has {num_items} {item_plural} in it:{item_descriptions}\n")
        else:
            print("There are no items in this room.\n")
    
    def try_add_item_to_inventory(self, item_name):
        for item in self.current_room.items:
            if item.name == item_name:
                self.inventory.append(item)
                self.current_room.items.remove(item)
                item.on_take()
                break
        else:
            print(f"\n...Erm, there is no item named \"{item_name}\" in this room.\n")

    def try_drop_item_from_inventory(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.current_room.items.append(item)
                self.inventory.remove(item)
                item.on_drop()
                print(f"The {item_name} is now in room: {self.current_room.name}.\n")
                break
        else:
            print(f"\n...Erm, you do not have an item named \"{item_name}\" in your inventory.\n")