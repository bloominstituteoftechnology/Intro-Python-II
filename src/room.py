# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self,name="empty", description="empty"):
        self.name = name
        self.description = description
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.n_to = None
        self.item_list=[]

    def add_item(self,item):
        self.item_list.append(item)

    def remove_item(self,item):
        self.item_list.remove(item)


    def show_item(self):
        print(f'This room has {len(self.item_list)} items:')
        for item in self.item_list:
            print(item.name)