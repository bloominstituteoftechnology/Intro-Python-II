# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room, inventory = []):
        self.current_room = current_room
        self.inventory = inventory

    def move(self, direction):
        new_room = self.current_room.adjacent_room_for(direction)
        self.current_room = new_room

    def look_around(self):
        self.current_room.list_visible_items()

    def view_inventory(self):
        print("\nYou currently have:")
        if len(self.inventory) < 1:
            print("Nothing...")
        else:
            for item in self.inventory:
                print(f'- {item}')