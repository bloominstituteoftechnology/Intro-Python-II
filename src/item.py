class Item:
        def __init__(self, name, description):
            self.name = name
            self.description = description

        def get(self):
            print(f'You have picked up {self.name}')
            
        def drop(self):
            print(f'You have dropped {self.name}')
        