from player import Player
from rooms import rooms


class Parser:
    """Parse user input into game commands."""
    def __init__(self, commands, player):
        self.commands = commands
        self.actions = ['move', 'look', 'get', 'take', 'drop', 'slash', 'use']
        self.directions = ['n', 's', 'e', 'w']
        self.current_player = player

    def parse(self):
        # TODO: Make this better.
        print(f"Okay, I'll try to {self.commands} \n")
        command = self.commands.split()

        if command[0] in self.actions:

            if command[0] == 'move':
                if len(command) < 2:
                    print("I need to know which direction to move. \n")
                    return
                if command[1] in self.directions:
                    return self.current_player.move(command[1])
                print("I couldn't understand. Which direction? \n")

            if command[1] in self.current_player.items:
                self.current_player.action(command[0], command[1:])
        print(f'Unknown action: {command[0]}')
        print(f'Available actions: {self.actions} \n')
        self.current_player.print_position()


def set_player(name=None):
    if not name:
        while True:
            try:
                name = input('What is your name? \n:')
                if not name == "":
                    break
                else:
                    print("I didn't catch that. \n")
                    continue
            except ValueError:
                print("I didn't understand that. \n")
                continue
    player = Player(name)
    return player


def get_player_input(player):
    while True:
        try:
            command = input('What should I do? \n:')
        except ValueError as e:
            print("I didn't understand that. \n")
            print(e)
            continue
        else:
            if command.lower().startswith('q'):
                break
            if command == "":
                print("Please, say something... I don't know what to do. \n")
                continue
        Parser(command.lower(), player).parse()
    print('Thanks for playing!')


def main(rooms):
    player = set_player()
    player.current_room = rooms['rest_stop']
    rooms['rest_stop'].characters[player.name] = player
    player.print_position()
    get_player_input(player)


if __name__ == '__main__':
    main(rooms)


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
