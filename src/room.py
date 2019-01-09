# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        print('You have chosen the room "{}", the room says "{}"'.format(name, description))
