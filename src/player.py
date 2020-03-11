# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
    

    def interact(self, interaction, item):
        pickup = ['Take', 'Pick up', 'Grab', 'Get']
        throwout = ['Toss', 'Remove', 'Drop', 'Trash']
        

        if interaction.lower() is in pickup:
            print(f'You pickup {item.name}!')
            print(f'It can be described as: {item.description}')
            self.inventory.append(item)
        elif interaction.lower() is in throwout:
            print(f'You get rid of {item.name}!')
            self.inventory.remove(item)
    

