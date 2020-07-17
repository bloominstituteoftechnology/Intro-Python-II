# A class to hold what items are in the rooms and held by the player

class Item:
    def __init__(self, item, description):
        self.item = item
        self.description = description

    def __str__(self):
        return f'It appears to be a {self.description}.'

    def get_item(self):
        player_items.append(self.item)
        room_items.remove(self.item)

    def drop_item(self):
        room_items.append(self.item)
        player_items.remove(self.item)