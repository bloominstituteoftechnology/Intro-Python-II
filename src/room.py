# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, storage):
        self.name = name
        self.description = description
        self.storage = storage
    
    def __str__(self):
        output = f"{self.name}\n"
        output += f"{self.description}\n"
        output += f"Objects: {', '.join([item.name for item in self.storage])}\n"
        output += "Exits to the: "
        output += " [North] " if hasattr(self, "n_to") else ""
        output += " [South] " if hasattr(self, "s_to") else ""
        output += " [East] " if hasattr(self, "e_to") else ""
        output += " [West] " if hasattr(self, "w_to") else ""

        return output

    def removeItem(self, item_name_to_remove):
        """
        Removes item from Room storage. Returns removed item, or False if not found.
        """
        items_to_keep = []
        item_found = None

        for item in self.storage:
            if item.name == item_name_to_remove:
                item_found = item
            else:
                items_to_keep.append(item)
        self.storage = items_to_keep
        
        if item_found:
            return item_found
        else:
            return False