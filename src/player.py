# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def __str__(self):
        return f"Your name is {self.name}, and you are {self.current_room}"
player1 = Player("Arash", "outside")
print(player1)

