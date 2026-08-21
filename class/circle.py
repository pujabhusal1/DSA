class Circle:
    def __init__ (self, radius):
        self.radius = radius
        self.pi = 3.14

    def get_area(self):
        return self.pi * self.radius * self.radius

mycircle = Circle(5)
assert mycircle.get_area() == 78.50

mycircle = Circle(3)
assert mycircle.get_area(),2 == 28.26
