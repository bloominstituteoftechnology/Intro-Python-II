# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, description, current_room, inventory=[]):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.inventory = inventory
    
    def interact(self, interaction, item):
        pickup = ['Take', 'Pick up', 'Grab', 'Get']
        throwout = ['Toss', 'Remove', 'Drop', 'Trash']


        if interaction.lower() in pickup:
            print(f'You pickup {item.name}!')
            print(f'It can be described as: {item.description}')
            self.inventory.append(item)
            self.current_room['items'].remove(item)
        elif interaction.lower() in throwout:
            print(f'You get rid of {item.name}!')
            self.inventory.remove(item)
            self.current_room['items'].append(item)
    
    def move(self, direction):
        self.current_room = direction
        print(f'Moving to the {self.current_room.name}\n')
    
    def welcome_player(self):
        print(f'\nWelcome {self.name}! You are currently in the {self.current_room.name}')

    def looper_info(self):
        print(f'\nYou are now in the {self.current_room.name}')

    def self_describe(self):
        print(f'''Name: {self.name}
        Current Room: {self.current_room.name}
        Inventory: {self.inventory}''')

    def check_inv(self):
        print(f'''You have: {', '.join(self.inventory)} on you''')