# Implement a class to hold room information. This should have name and
# description attributes.
from player import Player

class Room:
    def __init__(self, name, description, storage=[], n_to=None, w_to=None, e_to=None, s_to=None):
        self.n_to = n_to
        self.w_to = w_to
        self.e_to = e_to
        self.s_to = s_to
        self.name = name
        self.description = description
        self.storage = storage

    def


    # def pick_item(self, item):
    #     for i in self.storage:
    #         if item == i:
    #             self.storage.remove(i)
    #             print(f"You picked up {item}")
    #             return self.storage
    #         else:
    #             print(f"There's no such thing as {item}.")



    def __str__(self):
        return f"Name of room: {self.name}\n" \
               f"Description: {self.description}\n" \
               f"Stuff that room has: {self.storage}\n" \
               f"North: {self.n_to}\n" \
               f"West: {self.w_to}\n" \
               f"East: {self.e_to}\n" \
               f"South: {self.s_to}"

if __name__ == "__main__":
    a = Room("asdf", "asjd;kl;") # __str__ works
    print(a)