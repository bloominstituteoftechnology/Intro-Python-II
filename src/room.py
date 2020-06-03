# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    """A class to hold room information and description attributes."""
    def __init__(self, name, desc, n_to = None, e_to = None, s_to = None, w_to =None, items = None):
        self.name = name
        self.desc = desc
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to
        self.items = items
    def __str__(self):
        return f"{self.desc}"