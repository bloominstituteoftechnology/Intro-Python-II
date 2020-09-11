class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f"{self.name} - {self.description}"

    def take_item(self):
        print(f"You have picked up a {self.name}")
    
    def drop_item(self):
        print(f"You have dropped a {self.name}")