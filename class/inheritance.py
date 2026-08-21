from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def get_area(self):
        return self.length * self.length

    def get_length(self):
        return self.length

mySquare = Square(10)
assert mySquare.get_area() == 100