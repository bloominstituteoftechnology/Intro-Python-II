# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, location):
        self.location = location
        self.inventory = []

    def __str__(self):
        return (f'Your location is {self.location}. Your inventory is {self.inventory}')
    def add_to_inventory(self, item):
        self.inventory.append(item)
        self.print_inventory()
    def remove_from_inventory(self, item):
        self.inventory.remove(item)
        self.print_inventory()
        

    def print_inventory(self):
        print("Your inventory is", [f"{p.name}: {p.description}" for p in self.inventory])


 
   
    # def dict_from_class(cls):
    #     return dict((key, value) for (key, value) in cls.__dict__.items()
    #     if key not in _excluded_keys)
