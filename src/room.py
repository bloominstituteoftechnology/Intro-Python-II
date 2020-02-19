# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, direction=[]):
        self.name = name
        self.direction = direction

    def __str__(self):
        # print out something different if len(items)

        output = f'{self.name} has: ' 
        for i in self.direction:
            output += f'\n - {i}'

        return output