# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):

        self.name = name
        self.current_room = current_room
        self.item = []

    def get_item(self, item):
        self.item.append(item)
        # self.current_room.items.remove(item)

    def remove_item(self, item):
        return self.item.remove(item)

    def print_item(self):
        if len(self.item) >0:
            print(f'{self.name} has these items:')
            for i in self.item:
                print(i)
        
        else: 
            print ('No items in your inventory.')

    def __str__(self):
      s =  f'{self.name} is located  {self.current_room}'
      return s


    def move_player(self, room):
        self.room = room
        print(f'direction is {self.room}') 