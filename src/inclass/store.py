from category import Category

class Store:
    def __init__(self, name, categories):
        # attributes
        self.name = name
        self.categories = categories

    def __str__(self):
        #return f'{self.name} has {len(self.categories)} categories.'
        output = self.name
        i = 1
        for cat in self.categories:
            output += f'\n{i}. {cat}'
            i += 1
        output += f'\n{i}. exit'

        return output

    def __repr__(self):
        return f'{self.name} has {len(self.categories)} categories.'

my_store = Store("Pets Plus", [Category('food'),Category('costumes'),Category('toys')])
print(my_store)

# add input parser
selection = int(input("please select a category number:\n")) - 1


while(selection != len(my_store.categories)+1):
    selection = int(input("please select a category number:\n")) - 1
    print(f'you selected {my_store.categories[selection]}')