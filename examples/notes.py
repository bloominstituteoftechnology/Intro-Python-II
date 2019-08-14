# from category import Category

# class Store:
#     def __init__(self, name, categories):
#         # underscores make variables private
#         self._name = name 
#         self.categories = categories

#     def set_name(self, new_name):
#         # validate that the name is appropriate
#         self._name = new_name
        
#     # so that print(store) works
#     def __str__(self):
#         output = "welcome to " + self._name + '\n'
#         i = 1
#         for category in self.categories:
#             output += str(i) + ". " + category.name + "\n"
#             i += 1
#         output += str(i) + ". to quit"
    
#         return output


# # instantiate a store instance
# my_store = Store("The Dugout", [Category("Running"), Category("Baseball"), Category("Basketball")])
# my_store.categories.append(Category("Football"))
# print(my_store)

# selection = 0
# # while not quit
# while selection != len(my_store.categories) + 1: 
#     # Read user input
#     selection = input("Select the number of a department: ")
#     try:
#         # check that its a number, if not, handle error
#         selection = int(selection)
#         # check if selection is the quit option
#         if selection == len(my_store.categories) + 1:
#             print ("Thank you for shopping")
#             break
#         # check if selection is within category range
#         elif selection > 0 and selection <= len(my_store.categories):
#             print(my_store.categories[selection - 1])
#         # if all else fails, give error message
#         else:
#             print ("Please select a valid category.")
#     except ValueError:
#         # handle error for non number inputs
#         print("Please enter your choice as a number.")





