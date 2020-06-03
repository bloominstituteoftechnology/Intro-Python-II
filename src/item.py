# create a class for Item. give the item a name and description

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_item(self):
        return f'you have picked up {self.name}'
    
    def drop_item(self):
        return f'you have dropped {self.name}'

    def __rpr__(self):
        return f'Item Name is: {self.name}, Description: {self.description}'