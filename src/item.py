# This will be the base class for specialized item types
# to be declared later.


class Item():
    def __init__(self, name, description):
        self.name = name  # should be one word
        self.description = description
