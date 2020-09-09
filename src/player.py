# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, cur_rm):
        self.name = name
        self.cur_rm = cur_rm
    def __str__(self):
        return f'''
        ===== player ======
        name: {self.name}\n
        current room: {self.cur_rm.name}\n
        ===================
        '''