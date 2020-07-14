#from [filename] import [classname]
from category import Category

class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        output = f"{self.name} \n" + "Store categories include: \n"
        for i, c  in enumerate(self.categories):
            output += " " + str(i+1) + ". " + c.name + "\n"
        return output + " 5. Exit"
my_store = Store("\n Welcome to Leslie's Bodega! :) \n", [Category("Salad"), Category("Coffee"), Category("Donuts"), Category("Pizza")])
print(my_store)

selection = 0
while selection != len(my_store.categories) + 1:
    selection = input("\n<< Select the number of a category >> ")
    print("\n  The user selected ** " + str(selection) + " ** \n")
    try:
        # move casting to int into the try block 
        selection = int(selection)
        if selection == len(my_store.categories) + 1:
            print("Thanks for shoppping! \n")
        elif selection > 0 and selection <= len(my_store.categories):
            print("*** " + str(my_store.categories[selection - 1]) + " ***")
        else: 
            print(str(my_store) + "\n !! Please select a valid number !!")
    except ValueError: # error message
        print(str(my_store) + "\n !! Please eneter your choice as a number !!")
