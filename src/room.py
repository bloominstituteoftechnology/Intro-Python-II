# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def get_name(self):
        return f"{self.name}"

    def get_description(self):
        return f"{self.description}"

    def get_items(self):
        if self.items == []:
            return f"This room contains no items."
        else:
            stuff = "Room items:\n"
            for item in self.items:
                stuff += f"{item}\n"
            return stuff

    def take_item(self, stri):
        for obj in self.items:
            if obj.name == stri:
                self.items.remove(obj)
                return obj
        else:
            return "Invalid item in room."

    def add_item(self, item):
        self.items.append(item)


