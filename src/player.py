from item import LightSource


class Player():
    def __init__(self, name, curr_room, inv_list=[]):
        self.name = name
        self.curr_room = curr_room
        self.inv_list = inv_list
        return

    def add_item(self, item):
        item.on_take()
        self.inv_list.append(item)
        return

    def remove_item(self, item_name):
        for i in self.inv_list:
            if i.name == item_name:
                i.on_drop()
                self.inv_list.remove(i)
                return
        return

    def list_inventory(self):
        if len(self.inv_list) == 0:
            print('you are not carrying anything.')
        else:
            print("you are carrying:")
            for i in self.inv_list:
                print(i)
        return

    def in_inv(self, item_name):
        ex_ists = False
        for i in self.inv_list:
            if i.name == item_name:
                ex_ists = True
        return ex_ists

    def get_item(self, item_name):
        for i in self.inv_list:
            if i.name == item_name:
                return i
        return None

    def has_light(self):
        ex_ists = False
        for i in self.inv_list:
            if isinstance(i, LightSource):
                ex_ists = True
        return ex_ists
