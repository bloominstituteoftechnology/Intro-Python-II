# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f"You are currently in {self.name.upper()}.\nHINT: {self.description}"