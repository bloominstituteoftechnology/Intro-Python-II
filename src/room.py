# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def n_to(self):
        if self.name == "outside":
            self.name == "foyer"
        elif self.name == "foyer":
            self.name = "overlook"
        else:
            self.name = "treasure"

    def s_to(self):
        return self.name

    def e_to(self):
        return self.name

    def w_to(self):
        return self.name