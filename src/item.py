class Item:
        def __init__(self, name, description):
            self.name = name
            self.description = description

        
        def on_pick(self):
            print(f'You have picked up {self.name}, \n {self.description}')   

        def on_drop(self):
            print(f'You have dropped {self.name}')  