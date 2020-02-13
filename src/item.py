class Item():
    def __init__(self, item_name, item_descr):
        self.item_name = item_name
        self.item_descr = item_descr

    def get_item(self):
        print(f"Hey, you have {self.item_name}, this id {self.item_descr} ")

    def drop_item(self):
        print(f"Hey, you dropped {self.item_name}, this id {self.item_descr},  ")


