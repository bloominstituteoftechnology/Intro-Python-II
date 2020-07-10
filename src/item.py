
class Item:
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
    
    def on_take(self, item):
        print(f'You have successfully picked up {self.name}')

    def on_drop(self, item):
        print(f'You have dropped {self.name}')