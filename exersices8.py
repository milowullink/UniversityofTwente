class Quadfun:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        self.hasZero = a != 0 or b == 0

    def eval(self, x):
        return self.a * (x ** 2) + self.b * x + self.c

    def isLinear(self):
        return self.a == 0

    def getDerivative(self):
        return LinFun(2 * self.a, self.b)

    def __add__(self, other):
        return Quadfun(self.a + other.a, self.b + other.b, self.c + other.c)

if __name__ == "__main__":
    f = Quadfun(1, 2, 3)
    g = Quadfun(-1, 2, -1)
    h = f + g
    print(h.eval(10))