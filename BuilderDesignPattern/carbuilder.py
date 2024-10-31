from car import Car
class CarBuilder:
    def __init__(self):
        self.car = Car()
    def set_seats(self,n):
        self.car.seats=n
        return self
    def set_type(self,type):
        self.car.type=type
        return self
    def set_power(self,power):
        self.car.power=power
        return self
    def set_gear(self,gear):
        self.car.gear=gear
        return self
    def build(self):
        return self.car    