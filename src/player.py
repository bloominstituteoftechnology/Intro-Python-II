# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name,current_room):
        self.name=name
        self.current_room = current_room
        self.items=[]


    def get_items(self):
         return self.items


    def add_item(self,item):
        return self.items.append(item)


    def delete_item(self,item):
         return self.items.remove(item)


    def __repr__(self):
        return "Name : " + self.name + "\n Current Room :  " + str(self.current_room)+ "\n Your  Items: " + str(self.items)
