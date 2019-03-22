'''
created on 13/3/2019

author:linchen chen 
'''

from abc import *
from math import pi

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):

    def __init__(self, width,length):
        self._width = width
        self._length = length

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @property
    def area(self):
        return self._width * self._length

    @property
    def perimeter(self):
        return 2*(self._width + self.length)

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return (pi * (self._radius**2))

    @property
    def perimeter(self):
        return 2*pi*self._radius



if __name__ == '__main__':
    c = Circle(5)
    rec = Rectangle(5,4)
    print("circle has area: {0}, and perimeter: {1}".format(c.area, c.perimeter))
    print("rectangle has area: {0}, and perimeter: {1}".format(rec.area, rec.perimeter))
