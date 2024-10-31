import copy
from shape import Shape
class Rectangle(Shape):
    def __init__(self,color,l,b):
        super().__init__(color)
        self.l=l
        self.b=b
    def clone(self):
        return copy.deepcopy(self)
    def display(self):
        print(f"Color: {self.color}, Length: {self.l}, Breadth: {self.b}")
        