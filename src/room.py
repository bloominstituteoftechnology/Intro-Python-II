# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.description}"

    n_to = 0
    e_to = 0
    s_to = 0
    w_to = 0