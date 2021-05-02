from math import sqrt

class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter()/2
        return sqrt(half * (half - self._a)*(half - self._b) * (half - self._c))

def main():
    a, b, c = 3, 4, 5
    # 靜態方法和類方法都是通過給類發信息來調用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通過給類發信息來調用對象方法但是要傳入接受信息的對象作爲參數
        # print(Triangle.perimeter(t))
        print(t.area())
    else:
        print('No Triangle')

if __name__ == '__main__':
    main()
