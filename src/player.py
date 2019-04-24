# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room, inventory = []):
        self.current_room = current_room
        self.inventory = inventory
        if len(self.inventory) > 0:
            self.inventory.sort()

    def move(self, direction):
        new_room = self.current_room.adjacent_room_for(direction)
        self.current_room = new_room

    def look_around(self):
        print(self.current_room.name)
        self.current_room.list_visible_items()

    def view_inventory(self):
        print("\nYou currently have:")
        if len(self.inventory) < 1:
            print("Nothing...")
        else:
            for item in self.inventory:
                print(f'- {item}')

    def view_item_named(self, item_name):
        # Check the room first
        item = self.current_room.get_item_named(item_name)
        if item == None:
            # If the item isn't in the room, check the player's inventory
            item = next((item for item in self.inventory if item.name == item_name), None)
            if item is None:
                print("\nThat item isn't available.")
                return
        item.view()

    def add_item(self, item):
        self.inventory.append(item)
        self.inventory.sort()
        item.on_take()

    def drop_item(self, item):
        self.inventory.remove(item)
        item.on_drop()

    def take_item_named(self, item_name):
        item = self.current_room.get_item_named(item_name)
        if item is None:
            print("\nThat item isn't available.")
        else:
            print(f'\nAttempting to take the {item_name}')
            self.current_room.remove_item(item)
            self.add_item(item)
            print(f'The {item_name} is yours!')

    def drop_item_named(self, item_name):
        item = next((item for item in self.inventory if item.name == item_name), None)
        if item is None:
            print("\nYou don't have one of those.")
        else:
            print(f'\nAttempting to drop the {item_name}')
            self.current_room.add_items(item)
            self.drop_item(item)
            print(f'You dropped the {item_name}.')