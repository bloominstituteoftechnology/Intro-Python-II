# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room_name = "", room_description = "", room_items = []):
        self.room_name = room_name
        self.room_description = room_description
        self.room_items = room_items

    def print_items(self):
        if len(self.room_items) == 0:
            return "There are no items in this room"
        elif len(self.room_items) == 1:
            return "there is a {} here".format(self.room_items[0])
        elif len(self.room_items) == 2:
            return "there is a {} and {} in this room".format(self.room_items[0], self.room_items[1])
        else:
            return "there is also a {}".format(", ".join(item.item_name for item in self.room_items))


    def __repr__(self):
        return "{} \nRoom Description: {}".format(self.room_name, self.room_description)

    def __str__(self):
        return "{} \nRoom Description: {}".format(self.room_name, self.room_description)