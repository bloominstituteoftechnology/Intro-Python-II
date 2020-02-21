# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return f"{self.name} is currently in the {self.current_room.name}"

    def check_inventory(self):
        if len(self.items) > 0:
            output = f"\nInvetory:\n"
            for item in self.items:
                output += f"{item.name}"
            print(output)
        else:
            print("\nYour inventory is empty.")

    def take_item(self, item):
        self.items.append(item)
        print(f"\nYou take the {item.name}") 

    def drop_item(self, item):
        self.items.remove(item)
        print(f"\nYou drop the {item.name}") 