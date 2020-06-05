# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        output_str = "You are in the {}. {}."
        return (output_str.format(self.name, self.description))

    def get_items(self):
        output_str = "The following items are in the room: \n"
        for each in self.items:
            output_str += each.name + "\n"
        return (output_str.format(self.items))
    def get_item(self, itemName):
        for each in self.items:
            if each.name == itemName:
                return each
    def remove_item(self, itemName):
        for each in self.items:
            if each.name == itemName:
                self.items.pop(self.items.index(each))
                print(itemName + " has now been picked up.")
    def add_item(self, item):
                self.items.append(item)

