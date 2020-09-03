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
        elif mov == 'e':
            if hasattr(self.room, 'e_to'):
                self.room = self.room.e_to
        elif mov == 's':
            if hasattr(self.room, 's_to'):
                self.room = self.room.s_to
        elif mov == 'w':
            if hasattr(self.room, 'w_to'):
                self.room = self.room.w_to
        else:
            print(f"[Error] Unexpected Input: {mov}")
            print("Expected: n, e, s, w, q")