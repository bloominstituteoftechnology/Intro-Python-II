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
        itms = [item.name for item in self.items]
        return f'items: {itms}'

    def __repr__(self):
        line = '\n'+30*'-'+'\n'
        s_items = f"{self.name}\n{self.description}\n{self._print_items()}"
        s_no = f"{self.name}\n{self.description}\nThis room has no items."

        if self._has_items():
            return f"{line}{s_items}{line}"
        else:
            return f"{line}{s_no}{line}"
