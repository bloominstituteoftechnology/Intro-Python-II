class Item:
    #TODO: Add ability for item to have inventory.
    def __init__(self, name, description, iscontainer=False, isopen=False, islocked=True, isheavy=False, inventory=[]):
        self.name = name
        self.description = description
        self.iscontainer = iscontainer
        self.isopen = isopen
        self.islocked = islocked
        self.isheavy = isheavy
        self.inventory = inventory
    
    def __str__(self):
        return f"{self.description}"