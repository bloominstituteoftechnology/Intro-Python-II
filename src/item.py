from player import Player

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f'{self.name} - {self.description}'
    
    def item_taken(self):
        print(f'{self.name} has been added to your inventory!')
    
    def item_dropped(self):
        print(f'{self.name} has been dropped!')
    
class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value