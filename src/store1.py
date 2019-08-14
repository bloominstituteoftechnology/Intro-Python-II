# class Store
#     -name
#     -categories
#
# class Category
#     -type

from category import Category

class Store:
    def  __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        output = ""
        output += self.name + "\n"
        output += "    Categories" + "\n"
        for c in c.categories:
            output += "        " + c + "\n"
        return output
selection = 0
my_store = Store("Zach's Store", [Category("Running"), Category("Baseball"), Category("Basketball")])

while selection != len(my_store.categories) + 1:
    exit = len(my_store.categories) + 1
    selection = input("Select the number of a department. " )
    try:
        if int(selection) == len(my_store.categories) + 1:
            print("Thanks, Have a good day")
            break
        else:
            print( my_store.categories[int(selection) - 1])
    except ValueError:
        print("Please enter a number")





