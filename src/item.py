# This will be the base class for specialized item types to be declared later.
# The item should have name and description attributes.
# Hint: the name should be one word for ease in parsing later.

class Item:
    def __init__(self, item, itemDes):
        self.item = item
        self.itemDes = itemDes

    def __str__(self):
        return f"{self.item}: {self.itemDes}"