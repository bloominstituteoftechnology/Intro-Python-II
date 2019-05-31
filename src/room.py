# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to = None, s_to = None, e_to = None, w_to = None, items = []):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.w_to = w_to
        self.e_to = e_to
        self.items = items
    def __str__(self):
        return(f"You are in room {self.name} which has the description of {self.description}")
    def displayItems(self):
        items = []
        for item in self.items:
            items.append(item.name)
        return items