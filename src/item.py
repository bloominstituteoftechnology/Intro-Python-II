from room import Room
# room = {
#     'outside':  ["Outside Cave Entrance",
#                      "North of you, the cave mount beckons"],

#     'foyer':    ["Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""],

#     'overlook': ["Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to th
# e north, a light flickers in
# the distance, but there is no way across the chasm."""],

#     'narrow':   ["Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""],

#     'treasure': ["Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""],
# }


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to th
e north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# for k, v  in room.items():
#     print (v)
print(room['outside'].name)

print(player.current_room)
print(player.current_room.description)

# move = ['n', 's', 'e', 'w']
# while move == player_move:
#     print(player.name)
#     print(player.description)

#     player_move =input('Enter valid player move(n,s, e, w): ')
#     try:
#         player.name
        