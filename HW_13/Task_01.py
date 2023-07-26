from Exept_01 import ValueException

class Rectangle:
    def __init__(self, length, width = None):
        if width == None:
            self.width = self.length = length
        else:
            self.length = length
            self.width = width

    def perimeter_rectagle(self):
        if self.length <= 0 or self.width <= 0:
            raise ValueException(self.length, self.width)
        return 2 * (self.length + self.width)
        
    def area_rectagle(self):
        if self.length <= 0 or self.width <= 0:
            raise ValueException(self.length, self.width)
        return self.length * self.width

if __name__ == '__main__':  
    p1 = Rectangle(4, 2)
    print(p1.perimeter_rectagle())
    print(p1.area_rectagle())