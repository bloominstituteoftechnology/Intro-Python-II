from room import Room
from player import Player
from item import Item


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("--- Foyer",
                     """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("--- Grand Overlook",
                     """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("--- Narrow Passage",
                     """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("--- Treasure Chamber",
                     """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),

    'sphinx':   Room("--- Sphinx Chamber",
                     """Towering before you is a stunning sphinx. Its eyes glow as it looks down at you. There is no visible exit. In an impossibly deep voice, it utters, 'I have nothing for you. What do you bring me, Adventurer?'""")

}

# Put items in rooms
room['outside'].add_item('pebble')
room['foyer'].add_item('sword')
room['overlook'].add_item('coin')
room['narrow'].add_item('key')
room['treasure'].add_item('rope')

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Main
name = input('What is your name, adventurer? ')

player = Player(name, room['outside'])

print(f'--- Welcome, {player.name}! Your current location is: {player.room_info()}')

def item(player, item):
    interact = input('What would you like to do? (HINT: You may "take" or "ignore" an item.) ')
    interact = interact.lower()

    if interact == 'take':
        player.inventory.append(item)
        print(f'--- You now have {player.inventory} in your inventory.')
        player.current_room.item_taken(item)
        gameplay(player)
    elif interact == 'ignore':
        print('--- You leave it there.')
        gameplay(player)
    else:
        print('--- There seems to have been an error. Please try again.')
        gameplay(player)

def gameplay(player):
    direction = input('What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, Q to quit) ')
    direction = direction.lower()

    if direction == 'n':
        location = player.current_room.n_to
        if location != None:
            player = Player(name, location)
            print(player.room_info())
            gameplay(player)
        else:
            print('--- There is nothing to the north. Please choose a different direction.')
            gameplay(player)
    elif direction == 's':
        location = player.current_room.s_to
        if location != None:
            player = Player(name, location)
            print(player.room_info())
            gameplay(player)
        else:
            print('There is nothing to the south. Please choose a different direction.')
            gameplay(player)
    elif direction == 'e':
        location = player.current_room.e_to
        if location != None:
            player = Player(name, location)
            print(player.room_info())
            gameplay(player)
        else:
            print('There is nothing to the east. Please choose a different direction.')
            gameplay(player)
    elif direction == 'w':
        location = player.current_room.w_to
        if location != None:
            player = Player(name, location)
            print(player.room_info())
            gameplay(player)
        else:
            print('There is nothing to the west. Please choose a different direction.')
            gameplay(player)

    elif direction == 'i':
        print(player.investigate())
        object = player.investigate()[14:-1]

        if player.investigate() != "--- There is nothing here.":
            item(player, object)
        else:
            gameplay(player)

    elif direction == 'in':
        if player.inventory != []:
            print(f'--- You currently have {player.inventory} in your inventory.')
            command = input('You can "drop" an item or "use" an item. Please name the item. (Example: "use pebble") ')
            command = command.lower()
            action, thing = command.split(' ')[0], command.split(' ')[1]
            if action == 'drop':
                if thing in player.inventory:
                    player.inventory.remove(thing)
                    player.current_room.add_item(thing)
                    print(f'--- You currently have {player.inventory} in your inventory.')
                    gameplay(player)
                else:
                    print('--- There seems to have been an error. Please try again.')
                    gameplay(player)
            elif action == 'use':
                if thing == "rope":
                    if player.current_room.name == "--- Grand Overlook":
                        print('--- Success! You fashion a swing and lauch yourself across the chasm, landing safely on the other side.')
                        player.current_room = room['sphinx']
                        print(player.room_info())
                        gameplay(player)
                    else:
                        print(f'The {thing} does not do anything here.')
                        gameplay(player)
                elif thing == "sword":
                    if player.current_room.name == "--- Sphinx Chamber":
                        print('--- You draw your sword and manage to slay the sphinx with one quick slash.')
                        print('--- You leave the cave dirty and tired, but alive.')
                        print('--- Thanks for playing!')
                    else:
                        print(f'--- The {thing} does not do anything here.')
                        gameplay(player)
                elif thing == "coin":
                    if player.current_room.name == "--- Sphinx Chamber":
                        print('--- The sphinx contemplates your offering for a moment, then chuckles. "Congratulations, Adventurer." It gets to its feet and steps to the right, revealing a massive pile of treasure.')
                        print('--- You leave the cave richer than when you started, and solved the mystery of the long-lost treasure. Congratulations!')
                        print('--- Thanks for playing!')
                    else:
                        print(f'--- The {thing} does not do anything here.')
                        gameplay(player)
                elif thing == "key":
                    if player.current_room.name == "--- Sphinx Chamber":
                        print('--- The sphinx seems to smile as it silently stands and steps to the left, revealing a door. "You are truly worthy," it says. You step forward, unlock the door, and see a shimmering fountain.')
                        print('--- Congratulations, you have discovered the Fountain of Youth! You now have the ability to live forever.')
                        print('--- Thanks for playing!')
                    else:
                        print(f'--- The {thing} does not do anything here.')
                        gameplay(player)
                elif thing == "pebble":
                    if player.current_room.name == "--- Sphinx Chamber":
                        print('--- The laughter of the sphinx is the last thing you hear. It snaps you up in one bite.')
                        print('--- Oh no, you died! Please try again.')
                    else:
                        print(f'--- The {thing} does not do anything here.')
                        gameplay(player)
                else:
                    print(f'--- The {thing} does not do anything here.')
                    gameplay(player)
            else:
                print('--- There seems to have been an error. Please try again.')
                gameplay(player)
        else:
            print('You have nothing in your inventory.')
            gameplay(player)


    elif direction == 'q':
        print('--- Farewell, adventurer!')

    else:
        print('---There seems to have been an error. Please try again.')
        gameplay(player)

if __name__ == '__main__':
    gameplay(player)
