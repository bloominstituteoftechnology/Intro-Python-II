# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        readable = f"Current Room: {self.name} {self.description}\n"

        for i in self.items:
            readable += f"Available Items: {i}. {i.description}"
        return readable