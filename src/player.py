# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f"{self.name}, you are in the {self.current_room}"

    def change_room(self, direction):
        new_room = getattr(self.current_room, f"{direction}_to")
        if new_room:
            self.current_room = new_room
            print(f"\nYou are now in the {self.current_room}")
        else:
            print("...please choose a different direction")

    def item_add(self, item_name):
        for item in self.current_room.items:
            if item.name == item_name:
                self.items.append(item)
                self.current_room.item_remove(item)
                print(f">> {item} added to your bag")
            else:
                print(f">> There is no {item_name} in {self.current_room.name}")

    def item_remove(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                self.current_room.item_add(item)
                print(f">> {item} removed from your bag")
            else:
                print(f">> {item_name} is not in your bag")

    def get_items(self):
        if len(self.items) == 0:
            print("Your bag is empty")
        else:
            for item in self.items:
                print(f">> {item}")
