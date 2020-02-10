from shutil import get_terminal_size

# set screen size
cols, rows = get_terminal_size()


# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
    def __directions__(self):
        divider = "_" * (cols - 1)
        return  divider + "\n" \
                + f"{self.n_to.name if self.n_to else ' '}".center(cols) + "\n" \
                + f"{self.w_to.name if self.w_to else ' '}".ljust(cols) \
                + f"<-- You -->".center(cols) \
                + f"{self.e_to.name if self.e_to else ' '}".rjust(cols) + "\n" \
                + f"{self.s_to.name if self.s_to else ' '}".center(cols) + "\n" \
                + divider
                 # + \t\t {self.e_to.name if self.e_to else " "}
                 # \n         {self.s_to.name if self.s_to else " "}
                 # "
