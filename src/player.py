# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, room):
        self.room = room
        
    def __str__(self):
        return f"Room: {self.room.name}\nDesc: {self.room.description}"

    def changeRoom(self, mov):
        if mov == 'q':
            exit()
        elif mov == 'n':
            if hasattr(self.room, 'n_to'):
                self.room = self.room.n_to
            else:
                print("North is not a valid direction")
        elif mov == 'e':
            if hasattr(self.room, 'e_to'):
                self.room = self.room.e_to
            else:
                print("East is not a valid direction")
        elif mov == 's':
            if hasattr(self.room, 's_to'):
                self.room = self.room.s_to
            else:
                print("South is not a valid direction")
        elif mov == 'w':
            if hasattr(self.room, 'w_to'):
                self.room = self.room.w_to
            else:
                print("West is not a valid direction")
        else:
            print(f"[Error] Unexpected Input: {mov}")
            print("Expected: n, e, s, w, q")