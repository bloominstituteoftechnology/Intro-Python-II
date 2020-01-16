# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = []

    def __str__(self):
        display_string = ""
        display_string += f"\n----------------\n"
        display_string += f"\n{self.name}\n"
        display_string += f"\n{self.description}\n"
        display_string += f"\n{self.get_exits_string()}\n"
        return display_string

    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        return None

    def get_exits(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits

    def get_exits_string(self):
        return f"Exits: {', '.join(self.get_exits())}"

    # r0 = Room("Starting Room", "This is where you start!")
    # r1 = Room("Next room", "this is where you go!")
    # r2 = Room("Final Room", "This is where you end up")

    # r0.n_to = r1
    # r1.s_to = r0

    # r1.n_to = r2
    # r2.s_to = r1

    # player_location = r0

    # while True:
    #     print(player_location.name)
    #     print(player_location.desc)

    #     dir = input("enter a direction to move: ")
    #     if dir == 'n':
    #         player_location = player_location.n_to
    #     elif dir == 's':
    #         player_location = player_location.s_to
    #     elif dir == 'w':
    #         if player_location.w_to is None:
    #             print("You can't go that way")
    #         player_location = player_location.w_to
    #     elif dir == 'e':
    #         player_location = player_location.e_to
    #     else:
    #         print(f"{dir} is not a direction I'm aware of")
