"""Add capability to add Items to the player's inventory. 
The inventory can also be a list of items "in" the player, 
similar to how Items can be in a Room."""

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # def add_item(self, name):
    #     # take input

    #     # check if it is one word

    #     # add item

    #     # if not one word say try again

