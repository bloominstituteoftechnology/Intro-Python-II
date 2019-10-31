from textwrap import wrap


class color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


class Room:
    def __init__(self, name, description=""):
        self.name = name
        self.description = "\n".join(wrap(description, 80))
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __repr__(self):
        return f"Room({self.name})"

    def __str__(self):
        return f"{color.BOLD}{self.name}{color.END} : {self.description}"

