# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
from item import Item

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

        if num_items > 0:
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
        print(f'You are now at the {self.current_room.name}.')
        print(f"{self.current_room.description}")

        num_items = len(self.current_room.items)

        if num_items > 0:
            s = "\n    "
            item_descriptions = s + s.join(str(item) for item in self.current_room.items)
            item_plural = "item" if num_items == 1 else "items"
            print(f"You see {num_items} {item_plural} here:{item_descriptions}\n")
        else:
            print("There is nothing of interest here.\n")
    
    def try_add_item_to_inventory(self, item_name):
        #TODO: Add ability to take an item out of a container.
        for item in self.current_room.items:
            if item.name == item_name:
                if item.isheavy == False:
                    self.inventory.append(item)
                    self.current_room.items.remove(item)
                    item.take()
                    break
                else:
                    item.take()
                    break
            else:
                print(f"\nYou can't find the \"{item_name}\".\n")

    def try_drop_item_from_inventory(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.current_room.items.append(item)
                self.inventory.remove(item)
                item.drop()
                print(f"The {item_name} now lays on the ground.\n")
                break
            else:
                print(f"\nYou can't find the \"{item_name}\".\n")
    
    def look_at_inventory(self):
        if len(self.inventory) >= 1:
            for item in self.inventory:
                print(item.description)
        else:
            print("There are no items in your inventory.")

    def look_at_item(self, item_name):
        if item_name == 'self':
            print(self.__str__())
        else:
            for item in self.current_room.items or self.inventory:
                if item.name == item_name:
                    print(item.description)
                    break
            print(f"There is no {item_name} here.")

    def open_item(self, item_name):
        for item in self.current_room.items or self.inventory:
            if item.name == item_name and item.iscontainer == True:
                if item.islocked == False and item.isopen == False:
                    item.isopen = True
                    print(f"You open the {item.name}.")
                    break
                elif item.islocked == False and item.isopen == True:
                    print(f"The {item.name} is already open.")
                    break
                elif item.islocked == True:
                    print(f"The {item_name} is locked.")
                    break
            elif item.iscontainer == False:
                print("You can't open that.")
                break
            print(f"There is no {item_name} here.")
    
    def unlock_item(self, item_name, with_key):
        valid_key = False
        for key in self.inventory:
            if key.name == with_key and key.name == 'key':
                valid_key = True

        for item in self.current_room.items or self.inventory:
            if item.name == item_name and valid_key == True:
                if item.islocked == True:
                    item.islocked = False
                    self.inventory.remove(key)
                    print(f"You unlocked the {item_name}.\n")
                    break
                else:
                    print(f"You can't unlock the {item_name}.\n")
                    break
            elif item.name == item_name:
                print(f"You can't find the proper key.\n")
                break
            else:
                print(f"You can't find the {item_name}.\n")

           
    #TODO: look_in_item() functions
        
