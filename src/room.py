class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.item_list = []
        for item in items:
            self.item_list.append(item)

    def __repr__(self):
        return f'{self.name}\n\n{self.description}\n'

    def search_room(self):
        print('You search the room and find:')
        if len(self.item_list) == 0:
            print('Nothing')

        for index, item in enumerate(self.item_list):
            print(f'  {index+1}. {item}')
        print('\n')

    def check_room(self, item):
        if item in [i.lower() for i in self.item_list]:
            return True
        else:
            return False

    def remove_item(self, item):
        self.item_list.remove(item)

    def add_item(self, item):
        self.item_list.append(item)
