# Write a class to hold player information, e.g. what room they are in
# currently.
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self): 
        return f'{self.name}, {self.description}'

    def __repr__(self): 
        return f'(Item({self.name}, {self.description})'  

    def on_take(self):
        print(f'you took {self.name}')

    def on_drop(self):
        print(f'you dropped {self.name}')