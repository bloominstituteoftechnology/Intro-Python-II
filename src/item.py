class Item:
    #TODO: Add ability for item to have inventory.
    def __init__(self, name, description, iscontainer, isopen, islocked, isheavy):
        self.name = name
        self.description = description
        self.iscontainer = iscontainer
        self.isopen = isopen
        self.islocked = islocked
        self.isheavy = isheavy
    
    def __str__(self):
        return f"{self.name}: {self.description}"
    
    def take(self):
        if self.isheavy == True:
            print(f"\nThe {self.name} is too heavy to pick up.\n")
        else:
            print(f"\nYou pick up the {self.name}.\n")
    
    def drop(self):
        print(f"\nYou drop the {self.name}.\n")

    def is_in_container(self, value, container):
        self.value = False
        self.container = container
