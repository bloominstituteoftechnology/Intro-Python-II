class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    """
    Specs say the following:
    The room should also have n_to, s_to, e_to, and w_to attributes which point to the room in that respective direction.

    I'm confused on this. I was given starter code that connected the rooms correctly already. Am I supposed to be transferring that
    starting code into the Room class?
    """