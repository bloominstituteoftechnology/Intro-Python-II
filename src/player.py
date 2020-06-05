# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"{self.name}: {self.location}"

    def move(self, input):        
        if input == 'n':
            if self.location.n_to is not None:
                self.location = self.location.n_to
            else:
                print("\nThere's nothing in that direction!")
        elif input == 's':
            if self.location.s_to is not None:
                self.location = self.location.s_to
            else:
                print("\nThere's nothing in that direction!")
        elif input == 'e':
            if self.location.e_to is not None:
                self.location = self.location.e_to
            else:
                print("\nThere's nothing in that direction!")
        elif input == 'w':
            if self.location.w_to is not None:
                self.location = self.location.w_to
            else:
                print("\nThere's nothing in that direction!")
