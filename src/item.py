class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name}"

    # def __str__(self):
    #     return f'name: {self.name}, item:{self.description}'

    def take_item(self):
        print(f'You have picked up {self.name}')

    def drop_item(self):
        print(f'You have dropped {self.name}')