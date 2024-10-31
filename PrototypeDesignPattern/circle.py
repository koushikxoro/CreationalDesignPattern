from shape import Shape
import copy
class Circle(Shape):
    def __init__(self,color,r):
        super().__init__(color)
        self.r=r
    def clone(self):
        return copy.deepcopy(self)
    def display(self):
        print(f"Color: {self.color}, Radius: {self.r}")