# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes


room1 = Room('hallway', 'dark creepy')
print(room1.name)
print(room1.attributes)
print(room1)
