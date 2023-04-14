class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self._radius = radius
            self._diameter = 2 * radius
        elif diameter is not None:
            self._diameter = diameter
            self._radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be provided")

    def area(self):
        return 3.141516 * self._radius ** 2

    def perimeter(self):
        return 2 * 3.141516 * self._radius

r = float(input("Enter the radius: "))
c = Circle(radius=r)
print("Area:", c.area())
print("Perimeter:", c.perimeter())

d = float(input("Enter the diameter: "))
c = Circle(diameter=d)
print("Area:", c.area())
print("Perimeter:", c.perimeter())