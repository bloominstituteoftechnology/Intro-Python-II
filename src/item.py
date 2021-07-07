class Item:
    def __init__(self, name="", desc=""):
        self.name = name
        self.desc = desc

    def __str__(self):
        result = ""
        if self.name is not None:
            result += f"item name: {self.name}"
        if self.desc is not None:
            result += f" desc: {self.desc}"
        return result

    def __repr__(self):
        return f"name {self.name}, desc {self.desc}"