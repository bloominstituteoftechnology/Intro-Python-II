
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __repr__(self):
        return(f'{self.name}--{self.description}')

    def on_take(self):
        print(f'**Item msg: You have picked up {self.name}.**\n')
        return(True)
    
    def on_drop(self):
        print(f'**Item msg: You have dropped {self.name}.**\n')
        return(True)