# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(player, name, room):
        player.name = name
        player.room = room
        player.item = []

    def get_item(player, item):
        player.item.append(item)

    def remove_item(player, item):
        player.item.remove(item)

    def print_item(player, item):
        if len(player.item) > 0:
            print("Items in your inventory: ")
            for i in player.item:
                print(i)
        else:
            print("You don't seem to have any items!")

    def __str__(player):
        s = f'{player.name} is currently {player.room}'
        return s
