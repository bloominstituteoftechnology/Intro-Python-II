from player import Player
import textwrap

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

def look(player, item_name = None):
    if item_name is None:
        player.look_around()
    else:
        player.view_item_named(item_name)
    return True

def inventory(player):
    player.view_inventory()
    return True

def quit_game(player):
    return False

def print_commands(player):
    command_string = " | ".join('"{0}"'.format(w) for w in sorted(commands.keys()))
    paragraph = textwrap.fill(f'Things you can type:\n{command_string}')
    print(f'\n{paragraph}')
    return True

def take_item(player, item_name):
    player.take_item_named(item_name)
    return True

def drop_item(player, item_name):
    player.drop_item_named(item_name)
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
    'look': look,
    'l': look,
    'view': look,
    'inventory': inventory,
    'i': inventory,
    'take': take_item,
    't': take_item,
    'get': take_item,
    'drop': drop_item,
    'd': drop_item,
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
        else:
            verb = split_commands[0]
            if verb in commands:
                item_name = split_commands[1]
                function = commands[verb]
                function(self.player, item_name)
            else:
                print("\nThat isn't a valid command, try again.")
        
        return True