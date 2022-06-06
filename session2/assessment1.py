import math

def f1(x):
    return math.sin(x/10)

def f2(x):
    return x ** 4 - 12 * x ** 3 + 60 * x ** 2 - 80 * x + 37

def f3(x):
    return math.e ** x + abs(4 * x - 8)

def minimumf(f):
    l = -1
    m = 0
    r = 1
    y1 = f(l)
    y3 = f(0)
    y5 = f(r)
    while y1 < y3:
        m = l
        l = l - (r - l)
        y3 = y1
        y1 = f(l)
    while y5 < y3:
        m = r
        r = r + (r - l)
        y3 = y5
        y5 = f(r)
    while r - l > 1.0e-9:
        s = (1/2)*(l + m)
        t = (1/2)*(m + r)
        y2 = f(s)
        y4 = f(t)
        if y1 > y2 and y2 < y3:
            r = m
            m = s
            y5 = y3
            y3 = y2
        elif y2 > y3 and y3 < y4:
            l = s
            r = t
            y1 = y2
            y5 = y4
        else:
            l = m
            m = t
            y1 = y3
            y3 = y4
    return m

print(minimumf(f1))
print(minimumf(f2))
print(minimumf(f3))