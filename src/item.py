# This file contains the item class


class Item:
    # This will be the base class for specialized items later
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f" Item: {self.name} - {self.description}"

    def __str__(self):
        return f"{self.name}"
