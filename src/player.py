
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
                    item.on_take()
                    self.inventory.append(item)
                    self.current_room.contents.remove(item)
                else: print("That item isn't here!")
        elif cmd in ['leave', 'drop', 'throw']:
            for item in self.inventory:
                if item.name == item_name:
                    item.on_drop()
                    self.inventory.remove(item)
                    self.current_room.contents.append(item)
                else: print("You don't have that item!")
        
                

    def room_interaction(self, cmd):
        if cmd == 'search' and len(self.current_room.contents) > 0:
            print(f'You find {self.current_room.contents}!')
        elif cmd == 'search':
            print('You find nothing!')


    def change_room(self, direction):     
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

                