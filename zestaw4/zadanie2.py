from math import hypot, atan, sin, cos, sqrt

class Zespolona:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def conjugate(self):
        return self.__class__(self.r, -self.i)

    def argz(self):
        return atan(self.i / self.r)

        
    def __abs__(self):
        Zespolona (sqrt(self.r ** 2 - self.i ** 2), 0)

    def __repr__(self):
        return "Zespolona (" + str (self.r) + ", " + str (self.i) + ")"

    def __str__(self):
        return "(" + str (self.r) + ("+" if self.i > 0 else "") + str (self.i) + "j)"

    def __add__(self, other):
        if isinstance(other, Zespolona) :
            return self.__class__(self.r + other.r, self.i + other.i)
        else:
            return self.__class__(self.r + other, self.i)

    def __sub__(self, other):
        if isinstance(other, Zespolona) :
            return self.__class__(self.r - other.r, self.i - other.i)
        else:
            return self.__class__(self.r - other, self.i)

    def __mul__(self, other):
        if isinstance(other, Zespolona) :
            return self.__class__(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)
        else:
            return self.__class__(self.r * other, self.i * other)

    def __radd__(self, other):
        if isinstance(other, Zespolona) :
            return Zespolona (self.r + other.r, self.i + other.i)
        else:
            return Zespolona (self.r + other, self.i)

    def __rmul__(self, other):
        if isinstance(other, Zespolona) :
            return Zespolona (self.r * other.r, self.i * other.i)
        else:
            return Zespolona (self.r * other, self.i * other)

    def __rsub__(self, other):
        if isinstance(other, Zespolona) :
            return Zespolona (-self.r + other.r, -self.i + other.i)
        else:
            return Zespolona (-self.r + other, -self.i)

    def __eq__(self, other):
        if isinstance(other, Zespolona) :
            return (self.r == other.r and self.i == other.i)
        else:
            return (self.r == other and self.i == 0)

    def __ne__(self, other):
        if isinstance(other, Zespolona) :
            return self.r != other.r or self.i != other.i
        else:
            return self.r != other or self.i != 0

    def __pow__(self, other):
        res = self
        for i in range (other - 1):
            res *= self
        return res


def main():
    print("Liczby zespolone")
    a = Zespolona(2, 5)
    b = Zespolona(1, -3)
    print(a)
    print(b)
    b_copy = eval(repr(b))
    print(type(b_copy), b_copy.r, b_copy.i)
    print(a + b)
    print(a - b)
    print(a + 4)
    print(7 - a)
    print(a * 4)
    print(a * (-4))
    print(a == Zespolona(2, 5))
    print(a ==  b)
    print(a != b)
    print(a != Zespolona(2, 5))
    print(a ** 2)
    print(b ** 4)


if __name__ == "__main__":
    main()


# Liczby zespolone
# (2+5j)
# (1-3j)
# <class '__main__.Zespolona'> 1 -3
# (3+2j)
# (1+8j)
# (6+5j)
# (5-5j)
# (8+20j)
# (-8-20j)
# True
# False
# True
# False
# (-21+20j)
# (28+96j)