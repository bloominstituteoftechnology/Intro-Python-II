# Write a class to hold player information, e.g. what room they are in
# currently.

# attributes of a player
#     current room    
#     inventory

#Player holds an inventory list
class Player:
    def _init_(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.items = []
    def travel(self, direction)
        #will move player in direction if valid

        #Otherwise print error
        if direction in ["n", "s", "e", "w"]:
            next_room = self.current_room.get_room_in_direction(direction)
            if next_room is not None:
                self.current_room = next_room
            else:
                print("You cannot move in that direction")
