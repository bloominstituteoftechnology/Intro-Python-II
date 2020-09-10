# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def __str__(self):
        return f'''
===== player ======
name: {self.name}\n
current room: {self.current_room.name}\n
===================
'''
    def move(self, dir):
        print(f'player tries to move to {dir}')
        print('|||| opening the door ...||||')
        path = f'{dir}_to'
        if hasattr(self.current_room, path):
            self.current_room = getattr(self.current_room, path)
            print(f'player is now in {self.current_room.name}')
        else:
            print('\n'*2)
            print('x-x '*5, ' WARNING ', 'x-x '*5)
            print('there is no exit towards given direction')
            print('x-x '*5, ' WARNING ', 'x-x '*5)
            print('\n'*2)