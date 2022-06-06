#1a

people = [('Milo', 'Wullink', 18),('Sam', 'Baak', 20),('Lieke', 'Stoker', 19)]

#1b

def getAge(t):
    return t[2]


#1c

def sortListOnAge(l):
    orderedList = sorted(l, key=lambda tup: tup[2])
    return orderedList

print(sortListOnAge(people))

#2

def getMaxIndex(L):
    k = len(L)
    if L == []:
        return None
    else:
        r = 0
        for i in range(1,k):
            if L[i] > L[r]:
                r = i
        return r+1

print(getMaxIndex([3,10,5,11,9]))
print(getMaxIndex([1]))
print(getMaxIndex([]))
print(getMaxIndex([1,3,3,2]))

#3

def primeSieve(n):
    bools = [True] * n
    L = []
    for p in range(2,n):
        if bools[p]:
            L.append(p)
            for m in range(p,n,p):
                bools[m] = False
    return L

print(primeSieve(20))
print(primeSieve(100))
print(primeSieve(1000))
print(primeSieve(10000))

#4
def revertWords(text):
    words = text.rsplit(sep=None, maxsplit=- 1)
    k = len(words)
    for i in range(k):
        words[i] = words[i][::-1]
    string1 =" ".join(words)
    return string1

print(revertWords("Hi I am Milo"))
