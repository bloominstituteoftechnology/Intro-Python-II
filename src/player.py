# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, current_room=''):
        self.name = name
        self.current_room = current_room
        self.hp = 10
        self.inventory = []

    def item_interaction(self, cmd, item_name):
# item_cmds = ['get','take','leave','throw','swing','eat','drink']
        if cmd in ['get','take']:
            for item in self.current_room.contents:
                if item.name == item_name:
                    self.inventory.append(item)
                    self.current_room.contents.remove(item)
                    print(f'You take the {item_name}')
        elif cmd in ['leave', 'drop', 'throw']:
            for item in self.inventory:
                if item.name == item_name:
                    print(f'You drop the {item_name}')
                    self.inventory.remove(item)
                    self.current_room.contents.append(item)
        else: raise Exception
                

    def room_interaction(self, cmd):
        if cmd == 'search' and len(self.current_room.contents) > 0:
            print(f'You find {self.current_room.contents}!')
        elif cmd == 'search':
            print('You find nothing!')


    def change_room(self, direction):     
        # possible_commands = {
        #                 'n': 'player.current_room.n_to',
        #                 'e': 'player.current_room.e_to',
        #                 'w': 'player.current_room.w_to',
        #                 's': 'player.current_room.s_to',}
        if direction == 'n': 
                self.current_room = self.current_room.n_to
        elif direction == 'e':
                self.current_room = self.current_room.e_to
        elif direction == 'w':
                self.current_room = self.current_room.w_to
        elif direction == 's':
                self.current_room = self.current_room.s_to


    def __str__(self):
        return str(vars(self))

                