class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        return self.items

    def remove_item(self, item):
        del self.items[item]

    def __str__(self):
        if items is not None:
            return f''
        return f'{self.name}: {self.description}' 