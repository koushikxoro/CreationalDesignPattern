from cat import Cat
from dog import Dog
class AnimalFactoy:
    def create_animal(self, animal_type):
        if animal_type=="dog":
            return Dog()
        elif animal_type=="cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")
        
