class Item:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):

        return f'{self.id} Weapon name: {self.name}, Description: {self.description}'



    def print_items(self):
        print(f'{self.name}')
