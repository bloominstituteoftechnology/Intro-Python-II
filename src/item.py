class Item:
    def __init__(self,name,description):
        self.name = name
        self.description = description

    def on_take(self,itemName):
        print(f"You picked up: {itemName}")
    
    def on_drop(self,itemName):
        print(f"You dropped: {itemName}")

    def __str__(self):
        return f"{self.name}: {self.description}"