# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, title, name, description, items):
        self.title = title
        self.name = name
        self.description = description
        self.items = items

    def __repr__(self):
        output = ""
        output += "Room: " + self.name + "\n"
        output += "Description: " + self.description + "\n"
        if len(self.items) > 0:
            for i in range(0, len(self.items)):
                output += str(i + 1) + ". " + self.items[i] + "\n"
        return output
