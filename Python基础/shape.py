from abc import ABCMeta, abstractmethod
from math import pi


class Shape(object, metaclass=ABCMeta):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def perimeter(self):
        return 2 * pi * self._radius

    def area(self):
        return pi * self._radius ** 2

    def __str__(self):
        return '我是一个圆'


if __name__ == '__main__':
    shapes = [Circle(3)]
    for shape in shapes:
        print(shape)
        print('周长', shape.perimeter())
        print('面积', shape.area())
