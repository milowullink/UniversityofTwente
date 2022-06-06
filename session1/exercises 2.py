#exercise 1
x = 42
y = x == 42
print(y)
print(y and not y)
if y or not y:
    print('Hurray!')

#exercise 2
x = 2
def f(x):
    x = 42
    print('In f:', x)
f(x)
print('After f:', x)

x = 2
def g(y):
    x = 42
    y = 2*y + 2
    print('In g:', x, y)
g(x)
print('After g:', x)

x = 2
def h(y):
    global x
    x = 42
    y = 2*y + 2
    print('In h:', x, y)
h(x)
print('After h:', x)

def isPrime(p):
    if p < 2:
        return False
    else:
        i = 2
        while i <= p/2:
            if p % i == 0:
                return False
            else:
                i += 1
        return True

print(isPrime(13))

n = 20000
i = 1
while i <= n:
    if isPrime(i):
        print(i)
    i += 1

def factorial(n):
    if n == 0:
        return 1
    else:
        k = factorial(n-1)
        return n * k

print(factorial(12))

def binCoeffFactorial(n,k):
    if k > n:
        return "Wrong input"
    a = factorial(n)
    b = factorial(k)
    c = factorial(n-k)
    return a / (b * c)

print(binCoeffFactorial(6,2))

def binCoeffLoop(n,k):
    if k > n/2:
        k = n - k
    i = 1
    r = 1
    while i <= k:
        r = r * (n - i + 1)/i
        i += 1
    return r

print(binCoeffLoop(6,2))

#exercise 5

def isPythagoreanTriple(a,b,c):
    return (1<=a<=b<=c) and (a ** 2 + b ** 2 == c ** 2)

n = 1000
a = 1
k = 0
while a <= n:
    b = a
    while b <= n:
        c = round((a ** 2 + b ** 2)** 0.5)
        if c <= n:
            if isPythagoreanTriple(a,b,c):
                k += 1
        b += 1
    a += 1
print(k)