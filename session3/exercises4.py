#1

a=1
b=1
while a <= 100:
    while b <= 100:
        if b % a == 0:
            print('(',a,',',b,')')
        b += 1
    a += 1
    b = 1

#2

def setComplement(S,n):
    C = set({i: i for i in range(1, n+1)})
    for i in S:
        if i in C:
            C.remove(i)
    return C

print(setComplement({1,2,10},20))
print(setComplement({},20))
print(setComplement(set({i: i for i in range(1, 21)}),20))
print(setComplement(set({5*i: i for i in range(0,6)}),20))

#3

def multiples(t,n):
    S = set()
    k = len(t)
    for j in range(n+1):
        for i in range(k):
            if j % t[i] == 0:
                S.add(j)
    return S

print(multiples((3,5),20))
print(multiples((2,3,5,7,9),20))
print(multiples((1,2),20))
print(multiples((),20))

def  primeExponent(k,p):
    i=0
    while k % p == 0:
        k = k/p
        i += 1
    return i

#4

def isPrime(k):
    i = 2
    while i < k:
        if k % i == 0:
            return False
        i += 1
    return True

print(isPrime(2))

def primeFactorization(k):
    dict1 = dict()
    P = set()
    for p in range(2,k):
        if isPrime(p):
            P.add(p)
    for p in P:
        i = primeExponent(k,p)
        if i > 0:
            dict1[p] = i
    return dict1

print(primeFactorization(120))
print(primeFactorization(1))
print(primeFactorization(143))
print(primeFactorization(1190))