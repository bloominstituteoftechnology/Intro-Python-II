# Create a file called item.py and add an Item class in there.
# The item should have name and description attributes.
# Hint: the name should be one word for ease in parsing later.


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print('\n\nYou have picked up ' + self.name + '!')

    def on_drop(self):
        print('\n\nYou have put down ' + self.name + '.')
