# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, subtext):
        self.name = name
        self.subtext = subtext

    def __str__(self):
        return f"{self.name}"

    def print_description(self):
        return f"{self.subtext}"