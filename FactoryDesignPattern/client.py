from dogfactory import Dogfactory
from catfactory import Catfactory

if __name__ == "__main__":
    dog_factory = Dogfactory()  # Create an instance of DogFactory
    cat_factory = Catfactory()  # Create an instance of CatFactory

    dog1 = dog_factory.create_animal()  # Call on the instance, not the class
    dog2 = dog_factory.create_animal()
    cat1 = cat_factory.create_animal()
    cat2 = cat_factory.create_animal()
    dog1.speak()
    dog2.speak()
    cat1.speak()
    cat2.speak()
   
