# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, moves, attributes):
        self.name = name
        self.moves = moves
        self.attributes = attributes

    def room_placement(self):
        print("Hello I move " + self.moves)    
    


player1 = Player('George','west', 'strong and tall')
print(player1.name)
print(player1.attributes)
print(player1.room_placement())

