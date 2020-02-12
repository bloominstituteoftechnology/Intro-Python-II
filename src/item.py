class Item():
    def __init__(self, name, description, options, takeable=False):
        self.description = description
        self.name = name
        self.options = options
        self.takeable = takeable

        if self.takeable:
            self.options[f"Take {name}."] = {'default':f"You take {name}."}
            self.options[f"Drop {name}."] = {'default':f"You drop {name}."}
