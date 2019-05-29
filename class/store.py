# a terminal based store that has categories and categoris have products in them
# users needs to be able to input a category to a list the producrs in that category

# class for store that has names (string) and categories (list)
# from category import Category -> if we would be importing Category


class Store:
    def __init__(self, name, categories):
        # attrributes/fields
        self.name = name
        self.categories = categories

    def __str__(self):
        output = ""
        output += self.name + "\n"
        i = 1
        for c in self.categories:
            output += " " + str(i) + ". " + c.name + "\n"
            i += 1
        output += " " + str(i) + ". Quit\n"
        return output


class Category:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "No products available in " + self.name


s = Store("Connor's Store", [Category("Doges"), Category("Cats"), Category("Fish"),
                             Category("Turtle"), Category("Hedgehogs"), Category("Unicorns"), Category("Food"), Category("Pet Drugs")])

print(s)
selection = 0
while int(selection) != len(s.categories) + 1:
    selection = input("Select the number of department : ")
    print("The user selected " + str(selection))
    try:
        selection = int(selection)
        if selection == len(s.categories) + 1:
            print("Thanks for shopping!")
        elif selection > 0 and selection <= len(s.categories):
            print(s.categories[selection - 1])
        else:
            print("Please select a valid number")
    except ValueError:
        print("Please enter the number")
