# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, player = None):
        self.name = name 
        self.description = description
        self.player = player

    def __str__(self):
        return f"In the {self.name}, {str(self.description).lower()}"