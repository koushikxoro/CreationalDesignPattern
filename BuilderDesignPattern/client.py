from carbuilder import CarBuilder
from director import Director
if __name__ == "__main__":
    carbuilder=CarBuilder()
    director=Director(carbuilder)
    car1=director.build_sports_car()
    car2=director.build_suv()
    print(str(car1))

