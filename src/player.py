# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def set_name(self):
        self.name = input('Welcome, please submit your name to continue ')
        return self.name

    def get_name(self):
        print(f"Hey {self.name}")

    def set_current_room(self, room):
        self.current_room = room
        return self.current_room

    def get_current_room(self):
        print(f"you are in room: {self.current_room}")

    def get_player_instruction(self):
        return (
            f""" 
                ******* Instructions********
                You can only move north, south, west, east
                use:
                Input n to move north
                Input s to move south
                Input w to move west
                Input e to move east
                Input q to quit
                
                !!!!!!! Good luck !!!!!!!!!!!!
                """
             )
