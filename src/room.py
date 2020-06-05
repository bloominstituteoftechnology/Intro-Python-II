# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f'{self.name}'

    def print_description(self):
        return f'{self.description}'

    def list_items(self):
        if not self.items:
            print("there are no items to be found in this room")
        else:
            print("This room contains some items: ")
            for item in self.items:
                print(item.name)
                print(item.description)

