import math
import random
import matplotlib.pyplot as plt


class binDist:
    def __init__(self, n, p):
        self.n = n
        self.p = p

    def eval(self, k):
        return (math.factorial(self.n)/(math.factorial(k) * math.factorial(self.n - k))) * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def Exp(self):
        return self.n * self.p

    def plotExact(self):
        L = []
        for i in range(math.ceil(2 * self.Exp())):
            L.append(self.eval(i))
        plt.plot(L)
        plt.xlim(0, 2 * self.Exp())

    def plotSim(self, prec):
        dist = [0] * prec
        for i in range(prec):
            x = 0
            for j in range(self.n):
                if random.random() < self.p:
                    x += 1
            dist[x] += 1 / prec
        plt.plot(dist)
        plt.xlim(0, 2 * self.Exp())

if __name__ == "__main__":
    dist = binDist(200, 0.3)
    dist.plotSim(10000)
    dist.plotExact()
    plt.show()
