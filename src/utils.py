"""
BeWilder Utilities :: Misc utility functions
"""


def justify_center(content: str, width: int, symbol: str):
    """Centers string in symbol - width chars wide.
    
    :param content (str) : String to be centered.
    :param width (int) : Column width to center within.
    :param symbol (str) : Symbol to fill the space.
    :return (str) : Content, centered.
    """

    text = content
    lines = text.split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i].center(width, symbol)
    text = "\n".join(lines)
    return text


def table_printer(array: dict, title: str, left_width: int, right_width: int):
    """Formats dict or list - table of contents style.
    
    :param array (dict or list) : Dict or list to format into table.
    :param title (str) : Title to be centered at top of table.
    :param left_width (int) : Width of left side of table.
    :param right_width (int) : Width of right side of table.
    """

    print(f"{title}".center(left_width + right_width, "-"))

    if isinstance(array, list):
        for i, v in enumerate(array):
            print(str(k).ljust(left_width, ".") + str(v).rjust(right_width, "."))
    elif isinstance(array, dict):
        for k, v in array.items():
            print(str(k).ljust(left_width, ".") + str(v).rjust(right_width, "."))
    else:
        print("Unrecognized array type.")


def prompt(key_cmds, prompt: str = "What do you want to do?"):
    """Prompts the user for a command to move the Player.
    
    :param prompt [str] : Prompt to show, defaults to "What do you want to do?"
    :return (str) : Returns the user's input.
    """
    width = len(prompt)  # Width of the table is width of prompt
    # Prints out the available commands, table of contents style
    print()  # Blank line for visual separation
    table_printer(key_cmds, prompt, 20, 20)
    return input("> ")
