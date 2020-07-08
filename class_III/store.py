class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def print_welcome(self):
        print(f"Welcome to {self.name}!")

        for d in self.departments:
            print(d)


# should Department inherit from Store?
# In this case, may not be necessary bc there is not much functionality
# to inherit from Store
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

# Loop forever while the user is browsing through departments
# use the `input` function to prompt the user to select a department to browse
while True:
    # print a welcome message for the Store
    store.print_welcome()

    # get the department number user wants to visit
    selection = input("Which department would you like to visit?")

    # if the user types "quit", exits the program
    if selection == "quit" or selection == " quit":
        break

    chosen_department = store.departments[int(selection) - 1]

    print(f"You picked the {chosen_department.name} department.\n")

# Define room class - name, description