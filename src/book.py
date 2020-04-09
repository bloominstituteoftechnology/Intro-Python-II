from item import Item


class Book(Item):
    def __init__(self, name, description, contents, is_read=False):
        self.contents = contents
        self.is_read = is_read
        super().__init__(name, description)
