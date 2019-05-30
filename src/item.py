# Add an on_take method to Item.

# Call this method when the Item is picked up by the player.

# on_take should print out "You have picked up [NAME]" when you pick up an item.


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_drop(self, item):
        print(f"{item.name} has been dropped 💣")
