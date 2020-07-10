# HERE WE WILL DEFINE A MONSTER THAT CAN FIGHT AGANIST OUR PLAYER

class Monster:
    def __init__(self,current_location):
        self.hp = 20
        self.str = 2
        self.current_location = current_location
    
    
    def attack(self,player):
        atk = player.max_hp - self.str
        player.max_hp = atk

    def __str__(self):
        return f'HP: {self.hp}, attack {self.str}, location {self.current_location}'



if __name__ == "__main__":
    monstro = Monster('tu madrina')
    print(monstro)      