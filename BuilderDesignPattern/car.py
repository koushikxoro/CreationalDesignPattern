class Car:
    def __init__(self):
        self.seats=None
        self.power=None
        self.type=None
        self.gear=None
    def __str__(self):
        return f"Seats: {self.seats}, Power: {self.power}, Type: {self.type}, Gear: {self.gear}"