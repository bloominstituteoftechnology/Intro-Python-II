# Implement a class to hold room information. This should have name and
# description attributes.


class Room:

    def __init__(self, name, description): def __init__(self, name, description, items):
        self.name = name	        self.name = name
        self.description = description	        self.description = description
        self.items = []

    def __repr__(self): def __repr__(self):
        return f"{self.name}\n#########################\n{self.description}\n" return f"{self.name}\n#########################\n{self.description}\n"
