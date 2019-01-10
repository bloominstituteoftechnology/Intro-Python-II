# This file contains the item class


class Item:
    # This will be the base class for specialized items later
    def __init__(self, name, description):
        self.name = name
        self.description = description
