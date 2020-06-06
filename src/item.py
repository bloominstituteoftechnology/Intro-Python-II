

class Item :
    def __init__(self,name,description):
        self.name=name
        self.description = description

    def on_take(self):
        print( "You have picked up " + self.name)


    def on_drop(self):
        print('You have dropped ' +self.name)

    def __str__(self):
        return "Item Name: " + self.name + "\n description:" + self.description