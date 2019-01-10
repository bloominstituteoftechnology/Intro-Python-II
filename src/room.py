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

    def _print_items(self):
        items = ''
        for item in self.items:
            items += f"{item.name} \n {item.description} \n"
        return items

    def __repr__(self):
        if self._has_items():
            return f"{self.name} \n {self.description} \n {self._print_items()}"
        else:
            return f"{self.name} \n {self.description} \n This room has no items."
