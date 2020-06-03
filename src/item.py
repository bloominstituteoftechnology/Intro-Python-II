class Item():
    def __init__(self, name, description):
        self.name = str(name).strip().replace(" ", "") # Double whammy just to be sure
        self.description = str(description)