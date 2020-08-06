# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    def __init__(self, name, current_room, items =[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def next_move(self, direction):

        if direction == "N":
               if location.n_to is not None:
                   player.current_room = current_room.n_to
                   print(f"You went North!")
           elif direction == "E":
               player.current_room = current_room.e_to
               print()
           elif direction == "S":
               player.current_room = current_room.s_to
               print()
           elif direction == "W":
               player.current_room = current_room.w_to
           else:
               print("Uh oh, That is not a valid direction! Try again!")


    
