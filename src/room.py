# Implement a class to hold room information. This should have name and
# description attributes.

import item

class Room:

    n_to = 0
    e_to = 0
    s_to = 0
    w_to = 0
    items = []

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.description}"

    def add_items(self, items):
        self.items = items