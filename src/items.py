# A class to hold what items are in the rooms and held by the player

class Item:
    def __init__(self, item, description):
        self.item = item
        self.description = description

    def __str__(self):
        return f'{self.item}'