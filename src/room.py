# Implement a class to hold room information. This should have name and
# description attributes.
"""Will need the following:
name
description
items
"""


class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        # list of items in state
        self.item_list = []

        # adds item to the list when a user enters a room (hopefully)
        def add_item(self, item):
            self.item_list.append(item)

        # if a user picks up the item, remove it from the list
        def remove_item(self, item):
            self.item_list.remove(item)

        def display_item(self):
            # initualize empty output for user
            output = ''
            # if no item in room, display nothing
            if len(self.item_list) == 0:
                return None
            else:
                # display all items in the room for the user
                for item in self.item_list:
                    output += f"{item.name}"
            return output
