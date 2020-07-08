class Store:

    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def print_welcome(self):
        print(f"Welcome to {self.name}! Which department would you like to visit?")

        for d in self.departments:
            print(d)
            
class Department:
    def __init__(self, id, name, products):
        self.id = id
        self.name = name
        self.products = products
    
    def __str__(self):
        return f"{self.id}: {self.name}"

store = Store("The Dugout", [
    Department(1, "Baseball", []),
    Department(2, "Basketball", []),
    Department(3, "Football", []),
    Department(4, "Golf", [])
])

# loop forever while the user is browsing throguh departments
# use the 'input' function to prompt the user to select a department to browse
while True:
    # print a weclome message for the Store
    store.print_welcome()

    # get the department number the user wants to visit:
    selection = input("Which department would you like to visit? (1 for Baseball, 2 for Basketball, 3 for Football, 4 for Golf, 5 to quit program)")

    if int(selection) == 5:
        exit()

    print(f"You selected the {store.departments[int(selection)-1].name} Department")