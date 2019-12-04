from room import Room, room


class Player:
    """
    Holds player information.
    - What room they are in currently
    - What items they are holding
    """

    def __init__(self, player_name):
        self.player_name = player_name
        self.current_room = room['outside']
        self.items = []

    def announce(self):
        print(f'\nEntering "{self.current_room.name}"')
        print(f"Description: {self.current_room.description}\n")
        if len(self.current_room.items) > 0:
            for item in self.current_room.items:
                print(f"You see a {item.name} in the room.")
        else:
            print("Nothing worth taking in this room.")

    # def inventory(self, verb, obj):
    #   if self.verb in ['take','get','pick']:
    #     if self.obj in self.current_room.items:
    #       ds
    #     else:
    #       print(f"No {self.obj} to pick up.")
    #   elif self.verb in ['drop']:
    #     if self.obj in self.player.items:
    #       sdff
    #     else:
    #       print(f'No {self.obj} in inventory.')
    #   else:

    def move(self, direction):
        if direction == "N":
            if self.current_room.n_to != None:
                self.current_room = self.current_room.n_to
                print("\nHeading north...")
                return self.announce()
            else:
                print("\nNo way north...\n")
        elif direction == "E":
            if self.current_room.e_to != None:
                print("\nHeading east...")
                self.current_room = self.current_room.e_to
                return self.announce()
            else:
                print("\nNo way east...\n")
        elif direction == "S":
            if self.current_room.s_to != None:
                print("\nHeading south...")
                self.current_room = self.current_room.s_to
                return self.announce()
            else:
                print("\nNo way south...\n")
        elif direction == "W":
            if self.current_room.w_to != None:
                print("\nHeading west...")
                self.current_room = self.current_room.w_to
                return self.announce()
            else:
                print("\nNo way west...\n")
