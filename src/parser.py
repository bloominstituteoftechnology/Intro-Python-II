from player import Player

def move_north(player):
    player.move("north")
    return True

def move_south(player):
    player.move("south")
    return True

def move_east(player):
    player.move("east")
    return True

def move_west(player):
    player.move("west")
    return True

def look_around(player):
    player.look_around()
    return True

def inventory(player):
    player.view_inventory()
    return True

def quit_game(player):
    return False

def print_commands(player):
    command_string = "\n".join('"{0}"'.format(w) for w in sorted(commands.keys()))
    print(f'\nThings you can type:\n{command_string}')
    return True

commands = {
    'north': move_north,
    'n': move_north,
    'south': move_south,
    's': move_south,
    'east': move_east,
    'e': move_east,
    'west': move_west,
    'w': move_west,
    'look': look_around,
    'l': look_around,
    'inventory': inventory,
    'i': inventory,
    'quit': quit_game,
    'q': quit_game,
    'help': print_commands,
    '?': print_commands

}

class Parser:
    def __init__(self, player):
        self.player = player

    def parse_command(self, command):
        split_commands = command.split(" ")
        if len(split_commands) == 1:
            if command in commands:
                function = commands[command]
                return function(self.player)
            else:
                print("\nThat isn't a valid command, try again.")
        
        return True

    

            # if command == "north" or command == "n":
            #     move_north(self.player)
            # elif command == "south" or command == "s":
            #     self.player.move("south")
            # elif command == "east" or command == "e":
            #     self.player.move("east")
            # elif command == "west" or command == "w":
            #     self.player.move("west")
            # elif command == "1" or command == "first":
            #     self.player.move("first")
            # elif command == "look":
            #     self.player.look_around()
            # elif command == "inventory" or command == "i":
            #     self.player.view_inventory()
            # elif command == "quit" or command == "q":
            #     return False
            # elif command == "?":
            #     self.print_commands()