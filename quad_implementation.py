class Rectangle:
    def __init__(self, segment1, segment2):
        self.segment1 = segment1
        self.segment2 = segment2

    def get_area(self):
        return self.segment1 * self.segment2

    def __add__(self, rect):
        return self.get_area() + rect.get_area()


class Square(Rectangle):
    def __init__(self, segment):
        self.segment1 = segment
        self.segment2 = segment