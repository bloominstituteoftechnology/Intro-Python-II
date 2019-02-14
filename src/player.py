# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, curr_room):
        self.curr_room = curr_room
        self.item_list: []

# print player data
        def __repr__(self):
            return f"Player is in {self.curr_room}"

# add item to players state list
        def grab_item(self, item):
            self.item_list.append(item)

# remove item from player state lsit
        def drop_item(self, item):
            self.item_list.remove(item)
