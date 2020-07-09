class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []

    def get_item(self, item):
        self.location.remove_item(item)
        self.items.append(item)
        return f'You picked up {item.name}'

    def __str__(self):
        return f'{self.name}' 