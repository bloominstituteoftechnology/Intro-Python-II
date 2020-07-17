class Item: 
    def __init__(self, name, description):
        self.name = name
        self.description = description 

    def on_take(self): 
        item = self.name 
        print(f'You picked up {item}.')

    def on_drop(self): 
        item = self.name 
        print(f'You dropped {item}.')

    def __repr__(self): 
        return f'{self.name} - {self.description}'

