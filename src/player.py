
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

if __name__ == "__main__": 
    player_1 = Player(room='outside')
    print(player_1)
 