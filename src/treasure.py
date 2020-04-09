from item import Item


class Treasure(Item):
    def __init__(self, name, description, is_locked=True):
        self.is_locked = is_locked
        super().__init__(name, description)
