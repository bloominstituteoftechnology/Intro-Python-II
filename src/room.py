# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.list_items = []

    def add_item(self, item):
        self.list_items.append(item)

    def print_items(self):
        output = ""
        if len(self.list_items) == 0:
            return None
        else:
            for item in self.list_items:
                output += f"{item.name} "

        return output 