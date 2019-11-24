# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.hp = 100
        self.attk_pwr = 10
        self.defense = 10
        self.inventory = []
        self.helm = None
        self.chest = None
        self.gloves = None
        self.pant = None
        self.boot = None
        self.right_hand = None
        self.left_hand = None

    def __str__(self):
        output = f'Name: {self.name} \n'
        output += f'Current Room: {self.current_room}'
        return output

    def inspect_self(self):
        output = f'\n {self.name}s stats:\n'
        output += f'HP left: {self.hp}\n'
        output += f'Attack Power: {self.attk_pwr}\n'
        output += f'Defense: {self.defense} \n'
        return output

    def inspect_gear(self):
        output = f'\n {self.name}s Gear:\n'
        output += f'Helmet: {self.helm}\n'
        output += f'Chestplate: {self.chest} \n'
        output += f'Gloves: {self.gloves} \n'
        output += f'Leguards: {self.pant} \n'
        output += f'Boots: {self.boot} \n'
        output += f'Right Hand: {self.right_hand} \n'
        output += f'Left Hand: {self.left_hand} \n'
        return output

    def show_inventory(self):
        if self.inventory != 0:
            output = f'{self.name}s Inventory:'
            for item in self.inventory:
                output += f'{item}'
        else:
            output = 'Your inventory is empty'

        return output

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f'\n Added {item.name} to inventory. \n')

    def equip_armor_slot(self, item, slot):
        self.slot = item

        print(f'\n {item.name} added to {slot} slot')

        if slot == 'right_hand':
            self.attk_pwr = self.attk_pwr + item.attk_pwr
            print(f'Congratulations, your Attack Power is now {self.attk_pwr} \n')
        else:
            self.defense = self.defense + item.defense
            print(f'Congratulations, your defense is now {self.defense} \n')
        
        


