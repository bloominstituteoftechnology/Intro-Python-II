# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self,
                 name,
                 description,
                 n_to='',
                 s_to='',
                 e_to='',
                 w_to='',
                 items=[]):
        self.name = name
        self.description = description
        self.items = items
        return

    def __str__(self):
        return (self.description)

    def add_item(self, item):
        print('added item to', self.name)
        self.items.append(item)
        return

    def remove_item(self, item):
        self.items.remove(item)
        return

    def inventory(self):
        if len(self.items) == 0:
            print('there is nothing around....')
        else:
            print("looking around, you see.... ")
            for i in self.items:
                print(i)
        # print("\n")
        return
