# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to="nothing", e_to="nothing", s_to="nothing", w_to="nothing"):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.description}"