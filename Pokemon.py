# create Pokemon

class Pokemon:
    def __init__(self, name, primary_type):
        self.primary_type = primary_type
        self.name = name

    def __str__(self):
        return f"{self.name}"

print(Pokemon(name = "bulbasaur", primary_type = "Grass"))