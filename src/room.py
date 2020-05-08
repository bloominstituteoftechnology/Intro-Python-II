# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

    def __str__(self):
        return(f'{self.name}\n\n{self.description}\n\n' +
               ' '.join(list(self.exits.keys())))
