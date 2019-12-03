# Write a class to hold player information, e.g. what room they are in
# currently.
from functions import print_slow
from instantiate import room, items

class Player(object):
    def __init__(self):
      self.current_room = None
      self.items = []
      self.foundTruck = False

    def search(self):
        items_taken = 0
        if len(self.current_room.items) >= 1:
            for item in self.current_room.items:
                print(f'You found a {item.name}')
                takeItem = input('Take item? (Y/N): ')
                if takeItem[0].upper() == 'Y':
                    self.items.append(item.name)
                    print_slow(f'{item.description}\n')
                    print_slow(f'You took the {item.name}\nCheck your inventory with \'items\'\n\n')
                    items_taken += 1
            for _ in range(0, items_taken):
                self.current_room.items.pop(0)


        else:
            print_slow('After searching hard, you find nothing\n')

    def move(self, direction):
        if direction == 'N' and self.current_room.n_to.name == room['cybertruck'].name and all(x in self.items for x in [items['redkey'].name, items['greenkey'].name, items['bluekey'].name]) == True:
            slow_print('You use all three keys and open the door and walk in.\n')
            self.current_room = room['cybertruck']
            print_slow(f'{self.current_room.description}')
        elif direction == 'N' and self.current_room.n_to.name == room['cybertruck'].name and all(x in self.items for x in [items['redkey'].name, items['greenkey'].name, items['bluekey'].name]) != True:
            print_slow('Looks like you\'ll need some items first, you wonder if it has something to do with the colors on the door.\n')
        elif direction == 'N' and self.current_room.n_to.name != room['cybertruck'].name and all(x in self.items for x in [items['redkey'].name, items['greenkey'].name, items['bluekey'].name]) != True:
            if self.current_room.n_to != None:
                self.current_room = self.current_room.n_to
                print_slow(f'{self.current_room.description}\n')
            else:
                print_slow('There is no where to go that direction\n')
        elif direction == 'E':
            if self.current_room.e_to != None:
                self.current_room = self.current_room.e_to
                print_slow(f'{self.current_room.description}\n')
            else:
                print_slow('There is no where to go that direction\n')
        elif direction == 'S':
            if self.current_room.s_to != None:
                self.current_room = self.current_room.s_to
                print_slow(f'{self.current_room.description}\n')
            else:
                print_slow('There is no where to go that direction\n')
        elif direction == 'W':
            if self.current_room.w_to != None:
                self.current_room = self.current_room.w_to
                print_slow(f'{self.current_room.description}\n')
            else:
                print_slow('There is no where to go that direction\n')
        else:
            print(all(x in self.items for x in [items['redkey'].name, items['greenkey'].name, items['bluekey'].name]) == True)
        
    def checkInventory(self):
        if len(self.items) >=1:
            print(f"""Items: {', '.join(self.items)}""")
        else:
            print('you don\'t have any items yet')

