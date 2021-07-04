# Write a class to hold player information, e.g. what room they are in
# currently.

# def get_item(self, item_name):
# 	for i in self.inv_list:
# 		if i.name == item_name:
# 			return i
#     return None
# If the user enters get or take followed by an Item name, look at the contents of the current Room to see if the item is there.

# If it is there, remove it from the Room contents, and add it to the Player contents.

# If it's not there, print an error message telling the user so.


class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom
        self.items = []

    def all_items(self):
        my_items = []
        for item in self.items:
            my_items.append(item.name)
        return my_items

    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            # Hint: isinstance might help you figure out if there's a LightSource among all the nearby Items.
            if self.currentRoom.is_light == True or self.currentRoom.light_source is not None:
                print(
                    f"{self.currentRoom.name} has {self.currentRoom.all_room_items()} available")
            else:
                print("It's pitch black!")
        else:
            print("You cannot move in that direction.")

    def add_item(self, item):
        for room_item in self.currentRoom.items:
            if item == room_item.name:
                self.items.append(room_item)
                self.currentRoom.remove_item(room_item)
                print(f"{self.name}, you added 👉  {item}")

    def drop_item(self, item_to_drop):
        for item in self.items:
            if item.name == item_to_drop:
                self.items.remove(item)
                item.on_drop(item)
        print(f"can not drop {item_to_drop}")
