# Implement a class to hold room information. This should have name and
# description attributes.
class Thee_Room:
    def __init__(self, name, description):
# self.north = None
# self.south = None
# self.west = None
# self.east = None

# self.name = name 
# self.description = description

# def __string__(self):
#     return f"{self.name} , {self.description}"

        self.name = name 
        self.description = description
        self.items = []

    def where_am_i(self):
        print(f"*******************\n{self.name}\n\n\t{self.description}\n*******************")
        self.list_items()
        
    
    def list_items(self):
        if self.items ==[]:
            print(f"You don't see any items nearby")
        else:
            if len(self.items) > 1:
                print("You see several items")
                for x in self.items:
                    print(f"A {x.name}: it appears to be {x.description}")
            else:
                print("You spot an item...")
                for x in self.items:
                    print(f"A {x.name}: it appears to be {x.description}")


