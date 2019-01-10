#player needs a starting place and ability to move around map

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
    
    def __repr__(self):
        return f"Player is in {self.current_room}"

#if current room werent here computer would find out until run time.
