# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name: str, description: str):
        self.name = name
        self.desc = description

    def __getattr__(self, attr):
        if attr[-3:] == '_to':
            print(f"There isn't a room to the {attr.strip('_to')}")
            return self
        else:
            super().__getattr__()
