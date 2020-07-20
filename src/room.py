# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        if len(self.items) > 0:
            items_output = "This room has"
            for i, item in enumerate(self.items):
                items_output += " " + str(i+1) + "." + item
            return items_output
        else:
            return "There's nothing in this room."