import math

string = ""
boolean = True
r = 0
w = 0
l = 0
si = 0
class shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def get_color(self, color = "green"):
        self.color = color
        self.color = input("Choose a color: ")

    def set_color(self):
        return self.color

    def is_filled(self, filled:bool):
        if self.color == "green":
            self.filled = filled
            return self.filled
        else:
            return self.color

    def set_filled(self):
        return self.filled

    def to_string(self):
        return f"A Shape with color of {self.set_color()} and {self.set_filled()}"

class circle(shape):
    def __init__(self, color, filled, radius = 1.0):
        super().__init__(color, filled)
        self.radius = radius

    def get_radius(self):
        self.radius = int(input("Radius of a circle: "))

    def set_radius(self):
        return self.radius

    def get_area(self):
        return float(math.pi * (self.radius ** 2))

    def get_perimeter(self):
        return float(math.pi * self.radius * 2)

    def to_string(self):
        y = f"shape with an area= {self.get_area()} and perimeter= {self.get_perimeter()}"
        return f"A Circle with radius= {self.set_radius()}, which is a subclass of {y}"

class rectangle(shape):
    def __init__(self, color, filled, width=1.0, length=1.0):
        super().__init__(color, filled)
        self.width = width
        self.length = length

    def get_width(self):
        self.width = int(input("Width of rectangle:"))

    def set_width(self):
        return self.width

    def get_length(self):
        self.length = int(input("Length of rectangle:"))

    def set_length(self):
        return self.length

    def get_area(self):
        return float(self.length * self.width)

    def get_perimeter(self):
        return float(2*self.length + 2*self.width)

    def to_string(self):
        x = f"{self.set_width()}"
        y = f"shape with an area= {self.get_area()} and perimeter= {self.get_perimeter()}"
        z = f"{self.set_length()}"
        return f"A Rectangle with width={x} and length={z}, which is a subclass of {y}"

class square(rectangle):
    def __init__(self, color, filled, width, length, side= 1.0):
        super().__init__(color, filled, width, length)
        self.side = side

    def get_side(self):
        self.side = int(input("Side for square: "))

    def set_side(self):
        return self.side

    def get_area(self):
        return float(self.side ** 2)

    def get_perimeter(self):
        return float(4 * self.side)

    def to_string(self):
        a = f"{self. set_side()}"
        b = f"shape with an area= {self.get_area()} and perimeter= {self.get_perimeter()}"
        return f"A Square with side={a}, which is a subclass of {b}"


def main():
    s = shape(string, boolean)
    c = circle(string, boolean, r)
    rect = rectangle(string, boolean, w, l)
    sq = square(string, boolean, w, l, si)
    #shape
    s.get_color()
    s.set_color()
    s.is_filled(boolean)
    s.set_filled()
    #circle
    c.get_radius()
    c.set_radius()
    c.get_area()
    c.get_perimeter()
    #rectangle
    rect.get_width()
    rect.set_width()
    rect.get_length()
    rect.set_length()
    rect.get_area()
    rect.get_perimeter()
    #square
    sq.get_side()
    sq.set_side()

    return s.to_string(), c.to_string(), rect.to_string(), sq.to_string()


if __name__=="__main__":
    print(main())

