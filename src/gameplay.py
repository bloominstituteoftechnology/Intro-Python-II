def process_cmd(player, cmd):
    commands = {
    "take": player.take_item,
    "get": player.take_item,
    "drop": player.drop_item,
    "toss": player.drop_item,
    "throw": player.drop_item,
    "leave": not_implemented,
    "eat": not_implemented,
    "drink": not_implemented,
    "search": player.search_room,
    "move": player.change_room,
    }
    split_cmd = cmd.split()
    print(f'Executing:{split_cmd}')
    to_do = commands.get(split_cmd[0], False)
    if not to_do:
        print(f'I can\'t understand "{cmd}"')
    else: to_do(split_cmd[-1])
    

def not_implemented():
    print("Can't do that yet! Please wait for update.")

def print_surroundings(player):
    print('----Room-----\n')
    print(player.current_room.name)
    print(player.current_room.description, '\n')
    print('-----------\n')
    print('Current Inventory:', player.inventory)
    print('Room Contents', player.current_room.contents)

def fight(player, monster):
    pass
