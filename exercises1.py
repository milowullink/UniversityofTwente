#exercise 1
print("Hello world!")

#exercise 2
a = 100
b = 7

c = a / b
d = a // b
e = a % b
f = a ** b

print(c,d,e,f)

#exercise 3
x = 13
y = 42

x = y
y = x

print(x,y)

#exercise 4
two = 3
three = 2

if two < three:
    print('Q1:', two, '<', three)
elif two > three:
    print('Q1:', two, '>', three)
else:
    print('Q1:', two, '=', three)

two = two + three
three += 3

if two < three:
    print('Q2:', two, '<', three)
elif two > three:
    print('Q2:', two, '>', three)
else:
    print('Q2:', two, '=', three)

#exercise 5
i = 1
#while i > 0:
    #print(i)
    #i += 1

#exercise 6
i = 1
while i <= 111:
    if i % 2 == 0:
        if i < 10:
            print(i, 'has one digit and is even.')
        elif i < 100:
            print(i, 'has two digits and is even.')
        else:
            print(i, 'has three digits and is even.')
    else:
        if i < 10:
            print(i, 'has one digit and is odd.')
        elif i < 100:
            print(i, 'has two digits and is odd.')
        else:
            print(i, 'has three digits and is odd.')
    i += 1

#exercise 7
n = 1000000
x = 1
y = 1
z = 2

print(x)
print(y)
while z <= n:
    print(z)
    x = y
    y = z
    z = x + y