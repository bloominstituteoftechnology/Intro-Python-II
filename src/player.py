# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, dmg, race, archetype, lv=1, inv=[], current_room=''):
        self.name = name
        self.dmg = dmg
        self.race = race 
        self.archetype = archetype 
        self.lv = lv 
        self.inv = inv
        self.current_room = current_room 

    def __str__(self):
        if self.current_room == '': #if they are an enemy
            return f'They are {self.name}, a level {self.lv} {self.race} {self.archetype}.'
        return f'You are {self.name}, a level {self.lv} {self.race} {self.archetype}.'

    def getRoom(self):
        return self.current_room 

    def getAvailableRooms(self):
        directions = {}
  
        if hasattr(self.current_room, 'n_to'):
            directions['N'] = self.current_room.n_to.name

        if hasattr(self.current_room, 'w_to'):
            directions['W'] = self.current_room.w_to.name

        if hasattr(self.current_room, 's_to'):
            directions['S'] = self.current_room.s_to.name
    
        if hasattr(self.current_room, 'e_to'):
            directions['E'] = self.current_room.e_to.name

        return directions

    