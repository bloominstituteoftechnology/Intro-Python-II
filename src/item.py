class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}'
    # def take_item(self):
    #     print(f'You picked-up {self.name}')
    
    # def drop_item(self):
    #     print(f'You dropped the {self.name}')