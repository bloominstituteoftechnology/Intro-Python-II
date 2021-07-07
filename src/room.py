# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
    def __str__(self):
        return f'Room: {self.name}, description: {self.description}, items: {self.items}'

    def remove_item(self, item):
        for i in self.items:
            if i.name == item:
                self.items.remove(i)

    def add_item(self, item):
        self.items.append(item)




# The `Room` class should be extended with a `list` that holds the `Item`s
#     that are currently in that room.



