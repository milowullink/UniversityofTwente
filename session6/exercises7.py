class Person:
    def __init__(self,first,second,age):
        self.first, self.second, self.age = first, second, age

    def getInfo(self):
        return f'Information about {p.second}, {p.first}: age={p.age}'

singer = Person('Elvis', 'Presley', 42)
actor = Person('James', 'Dean', 24)
president = Person('John Fitzgerald', 'Kennedy', 46)
people = [singer, actor, president]

# Exercise 1b
for p in people:
    print(f'Information about {p.second}, {p.first}: age={p.age}')

# Exercise 1d
for p in people:
    print(p.getInfo())

class LinFun:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.hasZero = a != 0 or b == 0

    def eval(self, x):
        return self.a * x + self.b

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

f = Quadfun(3, 2, 1)
print(f.eval(4)) # 57
print(f.isLinear()) # False
f_prime = f.getDerivative()
print(f_prime.a)
print(f_prime.b)

g = Quadfun(0, 1, 2)
print(g.isLinear())