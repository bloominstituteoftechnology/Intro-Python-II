# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name="empty", description="empty"):
        self.name = name
        self.description = description

    def __str__(self):
        return f'room: {self.name}, description: {self.description}'

new_room = Room("outside", "it's the outside, what else is there?")
print(new_room)