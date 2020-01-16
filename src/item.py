# The item should have name and description attributes.

# Hint: the name should be one word for ease in parsing later.
# This will be the base class for specialized item types to be declared later.


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
