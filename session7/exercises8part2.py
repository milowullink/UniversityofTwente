import exersices8

if __name__ == "__main__":
    f = exersices8.Quadfun(1, 2, 3)
    g = exersices8.Quadfun(-1, 2, -1)
    h = f + g
    print(h.eval(10))