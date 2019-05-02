class Room:

    def __init__(self, title, details):
        self.title = title
        self.details = details
        self.inventory = []

    def __repr__(self):
        return f'{self.title}, {self.details}, {self.inventory}'

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)
