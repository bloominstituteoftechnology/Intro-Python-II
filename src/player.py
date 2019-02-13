# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, curr_room):
        self.room = curr_room

        def __str__(self):
            return f"{self.name} is in {self.curr_room}"
