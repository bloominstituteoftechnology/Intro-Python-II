# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, player=None):
        self.name = name
        self.description = description
        self.player = player
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"In the {self.name}, {str(self.description).lower()}"

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description
