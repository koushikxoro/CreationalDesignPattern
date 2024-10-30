from animalfactory import AnimalFactoy
class Catfactory(AnimalFactoy):
    def create_animal(self):
        return super().create_animal("cat")
    