from matrix import Matrix

def rsFinder(A, r, c):
    rs = r
    while rs < Matrix.numRows(A):
        if A[rs, c] != 0:
            return rs
        else:
            rs += 1
    return None

def gaussianElimination(A,b):
    r = 0
    c = 0
    L = []
    while r < Matrix.numRows(A) and c < Matrix.numCols(A):
        rs = rsFinder(A, r, c)
        if rs is not None:
            L.append((r, c))
            Matrix.swapRows(A, r, rs)
            Matrix.swapRows(b, r, rs)
            for i in range(r + 1, Matrix.numRows(A)):
                lamb = A[i, c] / A[r, c]
                for j in range(Matrix.numCols(A)):
                    A[i, j] -= lamb * A[r, j]
                b[i, 0] -= lamb * b[r, 0]
            r += 1
        c += 1
    while r < Matrix.numRows(A):
        if b[r, 0] != 0:
            return -1, None
        else:
            r += 1
    d = Matrix.numCols(A) - len(L)
    n = Matrix.numRows(b)
    x = Matrix(Matrix.numCols(A), 1)
    for p in reversed(L):
        xp = p[0]
        yp = p[1]
        ratio = A[xp, yp]
        for q in range(yp + 1, Matrix.numCols(A)):
            b[yp, 0] -= x[q, 0] * A[xp, q]
        x[yp, 0] = b[yp, 0] / ratio

    return d, x

def test_rs():
    print(rsFinder(Matrix([[0, 0, 0], [4, 5, 6]]), 0, 0))

if __name__ == '__main__':
    test_rs()