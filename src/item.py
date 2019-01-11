class Item:
    def __init__ (self, name, description):
        self.name = name
        self.description = description
        
    def __repr__ (self):
        return f"Name: {self.name}, description: {self.description}"

    def on_take(self):
        #add to player inventory
        print("taken")

    def on_drop(self): 
        #subtract from to room inventory
        print("dropped")

