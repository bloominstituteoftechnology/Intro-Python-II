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
        print(f'\nYou are at the {self.current_room.name}.')
        print(f"{self.current_room.description}")

        num_items = len(self.current_room.items)

        if num_items > 0:
            s = "\n    "
            item_descriptions = s + s.join(str(item) for item in self.current_room.items)
            item_plural = "item" if num_items == 1 else "items"
            print(f"You see {num_items} {item_plural} here: {item_descriptions}\n")
        else:
            print("There is nothing of interest here.\n")
    
    def add_item_to_inventory(self, item_name):
        for item in self.current_room.items:
            if item.name == item_name:
                if item.isheavy == False:
                    self.inventory.append(item)
                    self.current_room.items.remove(item)
                    print(f"\nYou pick up the {item.name}.\n")
                    break
                else:
                    print(f"\nThe {item.name} is too heavy to pick up.\n")
                    break
            else:
                print(f"\nYou can't find the {item_name}.\n")

    def get_item_from_container(self, item_name, container_name):
        for container in self.current_room.items or self.inventory:
            if container.name == container_name and container.iscontainer == True and container.islocked == False and container.isopen == True:
                for item in container.inventory:
                    if item.name == item_name:
                        container.inventory.remove(item)
                        self.inventory.append(item)
                        print(f"\nYou take the {item_name} out of the {container_name}.\n")
                        break
                    else:
                        print(f"\nYou can't find the {item_name} in the {container_name}.\n")
                        break
            elif container.islocked == True:
                print(f"\nThe {container_name} is locked.\n")
                break
            elif container.isopen == False:
                print(f"\nThe {container_name} is closed.")
            else:
                print("\nYou can't do that.\n")

    def put_item_in_container(self, item_name, container_name):
        for container in self.current_room.items or self.inventory:
            if container.name == container_name and container.iscontainer == True:
                for item in self.inventory:
                    if item.name == item_name:
                        container.inventory.append(item)
                        self.inventory.remove(item)
                        print(f"\nYou put the {item_name} in the {container_name}.\n")
                        break
                    else:
                        print(f"\nYou can't find the {item_name}.\n")
                        break
            else:
                print("\nYou can't do that.\n")
                break

    def drop_item_from_inventory(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.current_room.items.append(item)
                self.inventory.remove(item)
                print(f"\nYou drop the {item.name}.")
                break
            else:
                print(f"\nYou can't find the {item_name}.\n")
                break
    
    def look_at_inventory(self):
        if len(self.inventory) >= 1:
            for item in self.inventory:
                print(item.description)
        else:
            print("\nThere are no items in your inventory.\n")

    def look_at_item(self, item_name):
        if item_name == 'self':
            print(self.__str__())
        else:
            for item in self.current_room.items or self.inventory:
                if item.name == item_name:
                    print(item.description)
                    break
                else:
                    print(f"\nThere is no {item_name} here.\n")

    def open_item(self, item_name):
        for item in self.current_room.items or self.inventory:
            if item.name == item_name and item.iscontainer == True:
                if item.islocked == False and item.isopen == False:
                    item.isopen = True
                    print(f"\nYou open the {item.name}.\n")
                    break
                elif item.islocked == False and item.isopen == True:
                    print(f"\nThe {item.name} is already open.\n")
                    break
                elif item.islocked == True:
                    print(f"\nThe {item_name} is locked.\n")
                    break
            elif item.iscontainer == False:
                print("\nYou can't open that.\n")
                break
            print(f"\nThere is no {item_name} here.\n")
    
    def unlock_item(self, item_name, with_key):
        valid_key = False
        for key in self.inventory:
            if key.name == with_key and key.name == 'key':
                valid_key = True
                chosen_key = key

        for item in self.current_room.items or self.inventory:
            if item.name == item_name and item.iscontainer == True and valid_key == True:
                if item.islocked == True:
                    item.islocked = False
                    self.inventory.remove(chosen_key)
                    print(f"\nYou unlock the {item_name}.\n")
                    break
                else:
                    print(f"\nYou can't unlock the {item_name}.\n")
                    break
            elif item.iscontainer == False:
                print("\nThat is not a container.\n")
                break
            elif valid_key == False:
                print(f"\nYou can't find the proper key.\n")
                break
            else:
                print(f"\nYou can't find the {item_name}.\n")
                break


    def look_in_item(self, item_name):
        for container in self.current_room.items or self.inventory:
            if container.name == item_name and container.iscontainer == True:
                if container.islocked == True:
                    print(f"\nThe {item_name} is locked.\n")
                    break
                elif container.isopen == False:
                    print(f"\nThe {item_name} is closed.\n")
                    break
                else:
                    print(f"\nYou see the following item(s) in the {item_name}:")
                    if container.inventory == []:
                        print("None")
                        break
                    else:
                        for item in container.inventory:
                            print(item.description)
                        break
            else:
                print(f"\nSorry, {item_name} is not a container.\n")
                break
           
        
