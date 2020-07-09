# Implement a class to hold room information. This should have name and
# description attributes.
from textwrap import TextWrapper
textwrap = TextWrapper()
class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits

    def exit_to(direction):
        return True if direction in self.exits else False

    def __str__(self):
        return f"""{self.name}
        {textwrap.fill(self.description)}
        There are exits to the {", ".join(self.exits.keys()).upper()}."""
