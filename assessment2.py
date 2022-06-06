import string

# Exercise 1a

f = open('robinson-crusoe.txt')
data = f.read()
f.close()

dataInLines = data.splitlines()
k = len(dataInLines)
for i in range(k):
    print(dataInLines[i])

# Exercise 1d: This next part removes the punctuation and turns all capital into lower case letters.
def simplifyWord(word):
    simWord = word.translate(str.maketrans('', '', string.punctuation))
    simWord = simWord.lower()
    return simWord

# Exercise 1b: The main algorithm.

def wordStatistics(fileName):
    S = dict()
    dataInLines = fileName.splitlines()
    dataInLines = list(filter(lambda x: "CHAPTER" not in x,dataInLines)) # Exercise 1c
    k = len(dataInLines)
    for l in range(k):
        dataInWords = dataInLines[l].split()
        for w in dataInWords:
            sWord = simplifyWord(w)
            if sWord not in S:
                S[sWord] = 1
            else:
                S[sWord] += 1
    distWordCount = len(S)
    S = (sorted(S.items(), key=lambda kv:kv[1]))[::-1]
    b = S[50][1]
    while b >= 2:
        S = list(filter(lambda x: b not in x, S))
        b -= 1

    return distWordCount, S[:50], S[50:]

print(wordStatistics(data))