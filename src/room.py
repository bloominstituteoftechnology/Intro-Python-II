# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None


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
