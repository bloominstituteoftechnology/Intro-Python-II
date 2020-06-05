import random

def battleState():
    battleState = 1
    enemyIndex = random.randint(0,3)
    enemyList = [goblin, ghost, dragon, demonDog]
    attackList = [character.attack]