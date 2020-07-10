# Implement a class to hold room information. This should have name and
# description attributes.

# The room should also have n_to, s_to, e_to, and w_to attributes 
# which point to the room in that respective direction.

class Room:
    # n_to = "north"
    # s_to = "south"
    # e_to = "east"
    # w_to = "west"

    def __init__(self, name, description, room_items=[]):
        self.name = name
        self.description = description
        self.room_items = room_items

    def __str__(self):
        return f"LOCATION: {self.name} \nINFO: {self.description}"

    def view_items(self):
        print("\nITEMS IN ROOM: ")
        for i in self.room_items:
            i.print_name()

    def drop_item(self):
        for i in self.room_items:
            self.room_items.remove(i)



if __name__ == "__main__":
    room = {
        'outside':  Room("Outside Cave Entrance",
                        "North of you, the cave mount beckons"),

        'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
    passages run north and east."""),

        'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
    into the darkness. Ahead to the north, a light flickers in
    the distance, but there is no way across the chasm."""),

        'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
    to north. The smell of gold permeates the air."""),

        'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
    chamber! Sadly, it has already been completely emptied by
    earlier adventurers. The only exit is to the south."""),
    }

    print(room['treasure'])
    breakpoint()