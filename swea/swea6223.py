class Circle():
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return "원의 면적: {0}".format(self.radius ** 2 * 3.14)

circle = Circle(2)
print(circle.__repr__())
