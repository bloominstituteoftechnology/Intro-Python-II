class Item_list: 
    def __init__(self, name):
        self.name = name
        self.items = []
    def __str__(self):
        return f"{self.name}: {self.items}"
    def __repr__(self):
        return f"Item_list({repr(self.name)})"



quit = False

all_items = []

named_item = None

while not quit: 
    command = input("(C)reate a new item\n(S)elec your item {{current_item}}\n(Q)uit\nCommand:")    
    command.lower().strip()

    if command == 'q':
        quit = True 

    elif command == 'c': 
        name = input("Enter item name: ").strip()

        new_item = Item_list(name)
        all_items.append(new_item)

        print(all_items)
    
    elif command == 's':
        name = input("Enter item name: ").strip()
        
        named_item = None

        for i in all_items: 
            if i.name == name: 
                named_item = i 
                break #get out of for loop 

        if named_item is None: 
            print("No item named {name}")

        else: 
             current_item = named_item

        print(f">>> {current_item}")