# Implement a class to hold information. This should have a name and 
#description attributes

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return (f"{self.name}, item description: {self.description}")

    def __repr__(self):
        return self.name

    def pick_item(self):
        print(f'\n***You have picked up {self.name} to your inventory***')

    def drop_item(self):
        print(f'\n***You have dropped {self.name} from your inventory***')


    