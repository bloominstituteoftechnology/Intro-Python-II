# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap
class Room():
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
    def __str__(self):
        wrapped = textwrap.fill(self.description, 70)
        return f'''
Current Room: {self.name}
Description: {wrapped}
                '''