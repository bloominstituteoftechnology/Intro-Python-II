class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'Item: {self.name}, description of the item:{self.description}'
    
    def on_take(self):
        print(f'You have just picked up the {self.name}\n\n')
    
    def on_drop(self):
        print(f'you have just dropped the {self.name}\n\n')



    
