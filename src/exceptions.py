class MoveError(Exception):
    def __init__(self, room, direction):
        self.room = room
        self.direction = direction