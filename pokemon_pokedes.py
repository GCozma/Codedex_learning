class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
 
    def speak(self):
        print(f"{self.name} {self.name}!")
 
    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {', '.join(self.types)}")
        print(f"Description: {self.description}")
        if self.is_caught:
            print(f"{self.name} has already been caught!\n")
        else:
            print(f"{self.name} has not been caught yet!\n")
 
 
# --- Three Pokemon objects ---
 
pikachu = Pokemon(
    entry=25,
    name="Pikachu",
    types=["Electric"],
    description="It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.",
    is_caught=True
)
 
charizard = Pokemon(
    entry=6,
    name="Charizard",
    types=["Fire", "Flying"],
    description="It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.",
    is_caught=True
)
 
mewtwo = Pokemon(
    entry=150,
    name="Mewtwo",
    types=["Psychic"],
    description="It was created by a scientist after years of horrific gene-splicing and DNA-engineering experiments.",
    is_caught=False
)
 
# --- Using the methods ---
 
pikachu.speak()
pikachu.display_details()
 
charizard.speak()
charizard.display_details()
 
mewtwo.speak()
mewtwo.display_details()