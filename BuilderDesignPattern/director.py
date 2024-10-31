from carbuilder import CarBuilder
class Director:
    def __init__(self, builder:CarBuilder):
        self.builder=builder
    def build_suv(self):
        return (self.builder.set_seats(7).set_gear("Manual").set_gear(6).set_type("suv").build())
    def build_sports_car(self):
        return (self.builder.set_seats(2).set_gear("Automatic").set_gear(10).set_type("sports").build())
        