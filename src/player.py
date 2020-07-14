# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room):
        self.room = 'outside'

    def __str__(self):
        return f'You are currently in the {self.room} room'

if __name__ == "__main__": 
    player_1 = Player(room='outside')
    print(player_1)