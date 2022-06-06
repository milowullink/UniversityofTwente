#the print statement
print(1+1)

#large numbers
i=1414213562373

j = i * i
print(j)
k = j * j * j * j
print(k)

#operations
i=13
print(i/3)
print(3 / 3)

o = i // 3
print(o)

#modulo
p = 14 % 3
print(p)

#exponentiation
q = p ** 8
print(q)

#assignments
i = 1
i += 3
print("i is", i)
i *= 5
i -= 10
i /= 4
i **= 3
i %= 4
i //= 2
print("The new value of i is",i)

#if, elif, else
x = 5
if x%2 == 0:
    print(x,"is even")
else:
    print(x,"is odd")

x = 188
while x%2 == 0:
    print(x,"is even")
    x //= 2
print(x,"is odd")

#counting to 10!
i = 1
while i <= 10:
    print(i)
    i += 1

#booleans
b1 = True
b2 = False
print(b1 and b2)
print(b1 or b2)
print(not b1)
print(not b1 and not b2 or b1)
