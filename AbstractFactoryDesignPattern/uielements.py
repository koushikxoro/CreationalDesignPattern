from abc import ABC,abstractmethod
class Button(ABC):
    @abstractmethod
    def render(self):
        pass
class Textbox(ABC):
    @abstractmethod
    def render(self):
        pass