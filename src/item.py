# The item should have 'name' and 'description' attributes
    # The name should be one word for ease in parsing later
# This will be the 'base class' for specialized item types to be declared later

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {self.description}'

    