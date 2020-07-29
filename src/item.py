class Item:
    """
    This is the parent class for items
    """

    #constructor w/ positional args
    def __init__(self, name, description):
        self.name = name
        self.description = description

    
    def __str__(self):
        return f'{self.name}'

    
    def __repr__(self):
        return f'{self.name}'

    
    # method to print response on action completion
    def on_take(self):
        print(f"You have picked up {self.name} \n")

    
    # method to print response on action completion
    def on_drop(self):
        print(f'You have dropped {self.name} \n')