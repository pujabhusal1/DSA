class Square:
    """
    Length : 0-100
    """
    def __init__(self, length):
        self.length = length

    def get_area(self):
        return self.length * self.length

mySquare = Square(0) # Creates a square of length 10
assert mySquare.get_area() == 0

mySquare = Square(10)
assert mySquare.get_area() == 100

mySquare = Square(50)
assert mySquare.get_area() == 2500

mySquare = Square(100)
assert mySquare.get_area() == 10000

    