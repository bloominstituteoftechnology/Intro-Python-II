# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, item_list):
        self.name = name
        self.current_room = current_room
        self.item_list = []

    def drop(self):
        # print(self.item_list)

        drop_list = []

        for i, val in enumerate(self.item_list):
            print(i, "=", val)

        drop_index = int(input(
            "Please enter the number of the item you would like to drop: "))

        if drop_index <= len(self.item_list) and drop_index >= 0:
            dropped_item = self.item_list.pop(drop_index)
            drop_list.append(dropped_item)

        return drop_list

    def get_inventory(self):
        print(self.item_list)

    def __repr__(self):
        return f"name: {self.name}, current_room: {self.current_room}"
