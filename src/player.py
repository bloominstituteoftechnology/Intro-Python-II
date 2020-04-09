# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
            return (f' \n You are currently at the {self.current_room.name} \
                        \n {self.current_room.description}')

    def move(self, direction):
        new_room = getattr(self.current_room, f'{direction}_to')
        # print(new_room)
        if new_room == None:
            print('You cannot go that way. Please choose another direction')
        elif new_room is not None:
            self.current_room = new_room
            print("You have moved into the", self.current_room.name)
            print(self.current_room.description)
        

        