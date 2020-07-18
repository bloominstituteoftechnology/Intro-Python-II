# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def __str__(self):
        item_output = ""
        for item in self.items:
            item_output += f'\n{item}'
        return f'You are currently located in the {self.name}. {self.description}. The following item(s) are in this room: {item_output}'