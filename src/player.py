# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room, move):
        self.current_room = current_room
        self.move = move
    def entered(self):
        if hasattr(self.current_room, f"{self.move}_to"):
            self.current_room = getattr(self.current_room, f"{self.move}_to")
            # print(f"{self.move}_to")
            print(f"You entered {self.current_room.name}")
            print(f"Now {self.current_room.description}")
        else:
            print("There is nowhere place to go")

        
     