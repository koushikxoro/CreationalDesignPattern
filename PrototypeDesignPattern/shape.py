from abc import ABC, abstractmethod
class Shape:
    def __init__(self, color):
        self.color=color
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def clone(self):
        pass