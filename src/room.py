# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, unlocked=True, n_to=None, s_to=None, w_to=None, e_to=None, items=None):
        self.name = name
        self.description = description
        self.unlocked = unlocked
        self.items = [] if items is None else items

    def __str__(self):
        return f'This is the {self.name}'

    def has_item(self, item):
        for i in self.items:
            if i.name == item:
                return True
        return False

    def remove_item(self, item):
        self.items.remove(item)
