from room import Room
from player import Player
from os import system, name

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the entrance to the  the mansion awaits."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the  the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to the  north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """\n\nYou've found the long-lost treasure
chamber! Sadly, it has already been compl\netely emptied by
earlier adventurers. The only exit is to the  the south."""),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# --- clears console on game launch ---
def clearCon():
    #--nt is for windows
    if name == 'nt':
        _= system('cls')
    #--for mac and linux
    else:
        _= system('clear')

clearCon()

print("""Welcome to the  the adventure. In this game you will not be able to the  save your progress.
So lace those boots and lets and lets get moving.""")

#--- stringing capitalize and strip to the  clear white space and assure name is capital. ---
newPlayer = input("\nWhat is your name brave traveler?\n").capitalize().strip()
while len(newPlayer) < 2:
   newPlayer = input('\nPlease input at least a 2 character value for your name.\n').capitalize().strip()

#creates new Player instance with custom name.
Player1 = Player(newPlayer, room['outside'])
print(f'\nWelcome {Player1.name}. You are currently {Player1.current_room}\n')



input("Press any key to the  continue")

#--- dictionary for directions ---
directions = {
    'n': 'North',
    's': 'South',
    'e': 'East',
    'w': 'West',
    'q': 'Quit'
}
print('Type in the letter for the direction you would like to the  go:')
for options in directions:
    print(f'    {options} for {directions[options]}')
print('\n')

currentRoom = []
def roomChange():
    keys = room.keys()
    for i in keys:
        if str(i).capitalize() not in str(Player1.current_room):
            continue
        else:
            currentRoom.clear()
            currentRoom.append(i)
    # print(i)
    # print(Player1.current_room)

roomChange()

direction = ''

print('current room: '+ str(currentRoom[0]))

while direction != 'q':
    direction = input('Which way do you go   ----')
    try:
        selected = f'{directions[direction]}'
        if direction == 'n':
            Player1.current_room = Player1.current_room.n_to
            roomChange()
            print(f'\n\nYou head {selected} to the  {Player1.current_room}\n {room[currentRoom[0]].dialog}\n ')
        if direction == 's':
            Player1.current_room = Player1.current_room.s_to
            roomChange()
            print(f'\n\nYou head {selected} to the  {Player1.current_room}\n {room[currentRoom[0]].dialog}\n ')
        if direction == 'e':
            Player1.current_room = Player1.current_room.e_to
            roomChange()
            print(f'\n\nYou head {selected} to the  {Player1.current_room}\n {room[currentRoom[0]].dialog}\n ')
        if direction == 'w':
            Player1.current_room = Player1.current_room.w_to
            roomChange()
            print(f'\n\nYou head {selected} to the  {Player1.current_room}\n {room[currentRoom[0]].dialog}\n ')
            
    except KeyError:
        print(f"\nWhat in the heck is {direction}, try that again\n")
        for options in directions:
            print(f'    {options} for {directions[options]}')
        print('\n')
    except AttributeError:
        print('\nYou see that there is nothing in that direction and turn around.\n')



clearCon()
print(f'\n \nDust yourself off  {Player1.name}, we will see you again.\n \n')


