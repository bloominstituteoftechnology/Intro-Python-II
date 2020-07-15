# Implement a class to hold room information. This should have name and
# description attributes.

from collections import namedtuple

# Room = namedtuple("Room", "room_name room_description")

class Room:
    def __init__(self, room_name, room_description):
        self.room_name = room_name
        self.room_description = room_description


some_room = Room('foo', 'bar')

if __name__ == "__main__":
    print(some_room.__class__)