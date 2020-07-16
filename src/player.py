# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player():
    def __init__(self, room, name):
        self.room = room
        self.name = name

    # def __str__(self):
    #     if self.room == 'outside':
    #         return f'\nHello, {self.name}! You are {self.room}. {self.description}'
    #     elif self.room == 'treasure':
    #         return f'\nYou have found the {self.room}. {self.description}'
    #     else:
    #         return f'\nYou are in the {self.room}. {self.description}'

    def movement(self, decision):
        choice = self.movement_choice(decision)

        if choice is not None:
            self.room = choice
            print(self.room)

        else:
            print('There is only a wall there, try another direction...')