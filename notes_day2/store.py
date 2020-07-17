#from [filename] import [classname]
from category import Category
from product import Product
from clothing import Clothing

class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        output = f"{self.name} \n" + "Store categories include: \n"
        for i, c  in enumerate(self.categories):
            output += " " + str(i+1) + ". " + str(c) + "\n"
        return output + " 5. Exit"

my_store = Store("Leslies's Athletics", [Category("running", [Clothing("shoe", 100.00, "black", 10 ), Clothing("shorts", 50.00, "blue", "medium" ), Clothing("shirt", 20.00, "white", "medium" )]), Category("tennis"), Category("basketball")])

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
