class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return "사각형의 면적: {0}".format(self.width * self.height)

rectangle = Rectangle(4, 5)

print(rectangle.__repr__())