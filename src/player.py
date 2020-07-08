# Write a class to hold player information, e.g. what room they are in
# currently.


class Player(): 
    def __init__(self, player_name, current_room): 
        self.player_name = player_name
        self.current_room = current_room
        self.items = []


    def move(self, direction): 
        if getattr(self.current_room, f"{direction}_to") is not None: 
            self.current_room = getattr(self.current_room, f"{direction}_to")
        else: 
            print("There is no room in that Direction!")

    def pickup_item(self, item):
        if self.current_room.items.count(item) > 0:
            self.items.append(item)
            self.current_room.items.remove(item)
            item.pick_up()
        else:
            print(f"A {item.name} is not in this room.")

    def drop_item(self, item):
        if self.items.count(item) > 0:
            self.current_room.items.append(item)
            self.items.remove(item)
            item.drop()
        else:
            print(f"You do not have a {item.name} to drop.")

    def print_items(self):
        if not self.items:
            print("You have no items.")
        else:
            print("You have the following items: ")
            for x in self.items:
                print(x.name)