# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name,current_room):
        self.name = name
        self.current_room = current_room
        self.str = 10
        self.defense = 2
        self.magic = 8  
        self.lvl = 1
        self.exp = 0 
        self.max_hp = 25
        self.stat_points = 0

    def __str__(self):
        return f"{self.name} , {self.current_room}"  


    def try_movement(self,command):
        
        atribute = command + "_to"

    
        if hasattr(self.current_room, atribute):

            self.current_room = getattr(self.current_room, atribute)
            self.exp+=1

        else:
            print("you can't go that way!!")


    def lvl_up(self):
        base_exp = 10
        exp_multiplier = base_exp * self.lvl
        
        if self.exp >= exp_multiplier:
            self.lvl += 1
            self.max_hp += 10
            self.stat_points +=3


    def stats(self):
        return f'''
        level: {self.lvl}
        experience points: {self.exp}
        strenght: {self.str}
        defense: {self.defense}
        magic: {self.magic}
        HP: {self.max_hp}
        available stat points: {self.stat_points}
        
        
        '''        
    def attack(self,monster):
        atk = monster.hp - self.str
        monster.hp = atk

        # if exp_multiplier = self.exp:
        #     self.lvl += 1
        #     self.max_hp += 10
        #     self.stat_points +=3



        #se necesita cada vez que el jugador suba de nivel, la barra de exp subira x1.5

