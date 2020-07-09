import sys
from department import Department
from products import Product
from user import User

class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def print_welcome(self):
        print(f"\nWelcome to {self.name}!")

        for d in self.departments:
            print(d,"\n")





store = Store("The Dugout", [
    Department(1, "Baseball", [
        Product("Kid's Bat", 50),
        Product("Bat", 120),
        Product("Catcher's Mitt", 70),
    ]),
    Department(2, "Basketball", [
        Product("Basketball", 30),
        Product("Shorts", 20),
        Product("Jersey", 25)
    ]),
    Department(3, "Football", [
        Product("Football", 25),
        Product("Helment", 75),
        Product("Pads", 60)
    ]),
    Department(4, "Golf", [
        Product("Driver", 250),
        Product("Irons Set", 500),
        Product("Wedge Set", 300),
        Product("Putter", 150)
    ])
])

# Initialize a User
# use command line arguments to initialize a user
n = len(sys.argv)

if n < 2:
    money = 100
elif n == 2:
    money = sys.argv[1]
else:
    print("USAGE ERROR: store.py [money]")
    sys.exit(1)

# init user
user = User(money)

# Loop forever while the user is browsing through departments
# use the `input` function to prompt the user to select a department to browse
while True:
    # print a welcome message for the Store
    store.print_welcome()

    # print out the user's status
    print(f"{user.print_status()}\n")

    # get the department number user wants to visit
    selection = input("Which department would you like to visit? ")

    # if the user types "quit", exits the program
    if selection == "quit" or selection == " quit":
        break

    chosen_department = store.departments[int(selection) - 1]

    print(f"You picked the {chosen_department.name} department.\n")
    print("Here are the available products in this department:")
    products = chosen_department.products
    chosen_department.print_products()
    print()

    product_selection = input("Select a product to buy: ")

    # add the chosen product to the user's cart
    chosen_product = products[int(product_selection) - 1]
    user.add_to_cart(chosen_product)


# Define a User class
# Add the ability to select product and add them to the users
# cart
# Check the User's total amount of money before adding a product
# to their cart
# Subtract the price of the product from their money total