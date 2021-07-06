class Room:

    def __init__(self, title, description):
        
        self.title=title
        self.description=description
        self.items = []
    

        self.n_to=None
        self.e_to=None
        self.s_to=None
        self.w_to=None
        
        
    def where_am_i(self):
        print(f"*******************************************************************\n{self.title}\n\n\t{self.description}\n*******************************************************************")
        self.list_items()
        
    
    def list_items(self):
        if self.items ==[]:
            print(f"You don't see any items nearby")
        else:
            if len(self.items) > 1:
                print("You see several items")
                for x in self.items:
                    print(f"A {x.name}: it appears to be {x.description}")
            else:
                print("You spot an item...")
                for x in self.items:
                    print(f"A {x.name}: it appears to be {x.description}")