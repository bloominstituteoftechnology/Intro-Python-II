# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(room, name, description):
        room.name = name
        room.description = description

    def __str__(room):
        str = f'{room.name}: {room.description}'
        return str
