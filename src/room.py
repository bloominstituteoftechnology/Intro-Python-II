# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        itemsString = ""
        for item in self.items:
            itemsString += f"({item.name} - {item.description}), "

        return f"Room: {self.name}\nDesc: {self.description}\nItems: {itemsString[:-2]}"