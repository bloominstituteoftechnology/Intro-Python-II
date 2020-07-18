class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def take_item(self):
        print(f'You have picked up the {self.name}')

    def drop_item(self):
        print(f'You have dropped the {self.name}')

    def __str__(self):
        return f'item name: {self.name}, item description: {self.description}'