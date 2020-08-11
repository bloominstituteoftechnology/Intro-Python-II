# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, direction):
        self.name = name
        self.description = description
        self.direction = direction
        
    def __str__(self):
        return f"{self.name} where {self.description}."
