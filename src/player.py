# Class to manage a players name, current room, and items
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

    def __repr__(self):
        return self.name, self.location, self.inventory
    # Method to look in the player's current room for items

    def look(self):
        return self.location.inventory
        # Method to pick up an item in a room if any exists

    def pick_up_item(self, item_to_pickup):
        print(f'item_to_pickup: {item_to_pickup}')
        print(
            f'searching through self.location.inventory: {str(self.location.inventory)}')
        if item_to_pickup in str(self.location.inventory):
            self.inventory.append(item_to_pickup)
            return f'{item_to_pickup} picked up'
        else:
            return f'{item_to_pickup} does not exist.'
