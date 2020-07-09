# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room=None):
        # super().__init__()
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"{self.name}\n{self.current_room}"

    def move(self, direction):
        def wrong_way():
            print("It doesn't seem like we can go this way!")

        if direction.lower() == "n":
            if self.current_room.n_to:
                self.current_room = self.current_room.n_to
                print(self.current_room)
            else:
                wrong_way()

        elif direction.lower() == 's':
            if self.current_room.s_to:
                self.current_room = self.current_room.s_to
                print(self.current_room)
            else:
                wrong_way()
        elif direction.lower() == 'e':
            if self.current_room.e_to:
                self.current_room = self.current_room.e_to
                print(self.current_room)
            else:
                wrong_way()
        else:
            if self.current_room.w_to:
                self.current_room = self.current_room.w_to
                print(self.current_room)
            else:
                wrong_way()

