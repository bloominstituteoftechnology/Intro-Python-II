# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = 0
        self.s_to = 0
        self.w_to = 0
        self.e_to = 0

    def remove_item(self, item):
        self.items.remove(item)

    def __str__(self):
        returnString = f'You are located at {self.name} looking around {self.description}.'
        if len(self.items) > 0:
            returnString = returnString + f'There are items on the floor...\n'
            for i in self.items:
                returnString = returnString + f'{i.name}:{i.description}\n'
        return returnString