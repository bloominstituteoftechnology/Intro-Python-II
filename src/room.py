# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def _has_items(self):
        if len(self.items):
            return True
        else:
            return False

    def __repr__(self):
        if self._has_items():
            return f"{self.name} \n {self.description} \n {self.items}"
        else:
            return f"{self.name} \n {self.description} \n This room has no items."
