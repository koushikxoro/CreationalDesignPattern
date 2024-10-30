from animalfactory import AnimalFactoy
class Dogfactory(AnimalFactoy):
    def create_animal(self):
        return super().create_animal("dog")