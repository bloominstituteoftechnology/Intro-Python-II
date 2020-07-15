# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = None):
        self.name = name
        self.description = description
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
        return self.items
    
    def remove_item(self, item):
        self.items[item]

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}"

# def __repr__(self):
#     if items is not None:
#         return f""
#     return "{name: "+self.name+", description: "+self.description+"}"


room = Room("name", "description test")
print(room)
