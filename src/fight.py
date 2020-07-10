# FIGHTING FUNCTION

def fight(monster,player):
    while True:
        action = input('A monster has appeared!! Fight or flee?')

        if action == 'fight':
            monster.attack(player)
            print(f'the monstter has attacked you! your hp{player.max_hp}')
            player.attack(monster)
            print(f' YOUR ATTACK ITS EFFECTIVE MONSTER HP{monster.hp}')

        if action == 'flee':
            break

        if monster.hp == 0:
            print('you killed the monster!')
            break
            
    
    
        
        
