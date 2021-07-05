class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    

    def on_take(self):
        print("You picked up " + self.name)
    
    def on_drop(self):
        print("You dropped " + self.name)

    def __str__(self):
        print(f'Item: {self.name} - {self.description}')