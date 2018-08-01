"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积
"""
from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_vaild(a, b, c):
        return a + b > c and b + c > a and c + a > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        p = self.perimeter() / 2
        return sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))


if __name__ == '__main__':
    a, b, c = map(int, input('请输入三角形的三条边:').split())
    if Triangle.is_vaild(a, b, c):
        tri = Triangle(a, b, c)
        print('三角形周长%d' % tri.perimeter())
        print('三角形面积', tri.area())
    else:
        print('不是三角形')
