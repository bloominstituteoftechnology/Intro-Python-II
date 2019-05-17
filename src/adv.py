from room import Room
from player import Player

# Declare all the rooms

room = {
    'beyondthewall': Room("Beyond the wall", """North of you, the crashing mountains and endless snow overwehlm you. You know there are wildlings out there. The thought frightens you. Out of the corner of your eye you catch a glimpse of something moving. When you look back you see them! So many men... no... not men. They are all dead with ice blue eyes. You must go back to castle black, and warn the others! """),

    'castleblack': Room("Castle Black", "The men of the nights watch are all around you in their black cloaks, their swords dangling at their hip. You've told the night watch abut the force coming for them, but nobody believes you. You must head south to find someone who will."),

    'eastwatch': Room("Eastwatch", """The Wall drops into an inlet of the Shivering Sea called the Bay of Seals. It is deserted here. But you get clouded with a vision, a dragon, breathing blue fire will destroy this castle if it isn't stopped. There is nowhere to go but the way you came."""),

    'shadowtower': Room("The Shadow Tower", """Something feels eerie here. There is nowhere to go but the way you came.."""),

    'winterfell': Room("Winterfell", """You walk through the gates to a giant stone castle. Soldiers and children going this way, and that. Everything seems... right here. But you know with every fiber of your being, that if you don't do something, all these people will die."""),

    'thetwins': Room("The Twins", """You walk through the gates to a giant stone castle. Soldiers and children going this way, and that. Everything seems... right here. But you know with every fiber of your being, that if you don't do something, all these people will die."""),

    'blazewaterbay': Room("Blazewater Bay", """You walk through the gates to a giant stone castle. Soldiers and children going this way, and that. Everything seems... right here. But you know with every fiber of your being, that if you don't do something, all these people will die."""),

    'hornwood': Room("Hornwood", """You walk through the gates to a giant stone castle. Soldiers and children going this way, and that. Everything seems... right here. But you know with every fiber of your being, that if you don't do something, all these people will die."""),

    'theriverlands': Room("The Riverlands", """You walk through the gates to a giant stone castle. Soldiers and children going this way, and that. Everything seems... right here. But you know with every fiber of your being, that if you don't do something, all these people will die."""),

    'theeyrie': Room("The Eyrie", """You walk through the gates to a giant stone castle. Soldiers and children going this way, and that. Everything seems... right here. But you know with every fiber of your being, that if you don't do something, all these people will die."""),

    'ironislands': Room("The Iron Islands", """You walk through the gates to a giant stone castle. Soldiers and children going this way, and that. Everything seems... right here. But you know with every fiber of your being, that if you don't do something, all these people will die."""),
}


# Link rooms together

room['beyondthewall'].s_to = room['castleblack']

room['castleblack'].n_to = room['beyondthewall']
room['castleblack'].s_to = room['winterfell']
room['castleblack'].e_to = room['eastwatch']
room['castleblack'].w_to = room['shadowtower']

room['winterfell'].n_to = room['castleblack']
room['winterfell'].s_to = room['thetwins']
room['winterfell'].e_to = room['blazewaterbay']
room['winterfell'].w_to = room['hornwood']

room['thetwins'].n_to = room['winterfell']
room['thetwins'].s_to = room['theriverlands']
room['thetwins'].e_to = room['theeyrie']
room['thetwins'].w_to = room['ironislands']


#
# Main
#


# Make a new player object that is currently in the 'outside' room.
player = Player("John Snow", room["beyondthewall"])
# Write a loop that:
while True:
#
# * Prints the current room name
    print(player.room.name)
    print('current items:')
    print(player.bag)
    print('avalible items:')
    print(player.room.items)
# * Prints the current description (the textwrap module might be useful here).
    print(player.room.description)
# * Waits for user input and decides what to do.

    direction = input("Which way do you want to go? NSEW or Q to quit:")
    print(direction)
#
# If the user enters a cardinal direction, attempt to move to the room there.
    if direction == 'n' or direction == 's' or direction == 'e' or direction == 'w' or direction == 'q':
        if direction == "n":
            player.room = player.room.n_to
        elif direction == "s":
            player.room = player.room.s_to
        elif direction == "e":
            player.room = player.room.e_to
        elif direction == "w":
            player.room = player.room.w_to
# If the user enters "q", quit the game.
        elif direction == "q":
            print("you've ended the game")
            break
        elif direction == 'get':
            player.bag.append(direction)
            print('You just picked up an item')
# Print an error message if the movement isn't allowed.
#
        else:
            print('not a valid direction, please use n, s, e, or w.')
