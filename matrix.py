class Matrix:
    # Exercise 1a
    def __init__(self, first, second=None):
        self.L = []
        if second is None and type(first) == list:
            self.L = first
            self.m = len(self.L)
            self.n = len(self.L[0])
        elif type(first) == int and type(second) == int:
            self.m = first
            self.n = second
            for i in range(self.m):
                a = []
                for j in range(self.n):
                    a.append(0)
                self.L.append(a)
        else:
            print("Wrong input")

    # Exercise 1b
    def numRows(self):
        return self.m

    def numCols(self):
        return self.n

    #Exercise 1c
    def __getitem__(self, item):
      return self.L[item[0]][item[1]]

    def __setitem__(self, item, value):
      self.L[item[0]][item[1]] = value

    #Exercise 1d
    def swapRows(self, row1, row2):
        k = self.L[row1]
        self.L[row1] = self.L[row2]
        self.L[row2] = k

    def swapCols(self, col1, col2):
        p = []
        for i in range(self.m):
            p.append(self.L[i][col1])
            self.L[i][col1] = self.L[i][col2]
            self.L[i][col2] = p[i]

    #Exercise 1e
    def __add__(self, other):
        C = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                C[i,j] = self[i,j] + other[i,j]
        return C

    #Exercise 1f
    def __mul__(self, other):
        C = Matrix(self.m, other.n)
        for i in range(self.m):
            for j in range(other.n):
                for k in range(self.n):
                    C[i,j] += (self[i,k]*other[k,j])
        return C

    #Exercise 1g
    def __eq__(self, other):
        if self.m != other.m or self.n != other.n:
            return False
        else:
            for i in range(self.m):
                for j in range(self.n):
                    if self.L[i][j] != other.L[i][j]:
                        return False
            return True

    def __str__(self):
        line = ''
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                line += ' ' + str(self[i,j])
            line += '\n'
        return line


def test_init():
    A = Matrix(4, 3)  # Should create a 4-by-3 zero matrix.

    B = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # Should create a 3-by-3 identity matrix.

    C = Matrix([[1, 2, 3]])  # Should create a 1-by-3 matrix.

    D = Matrix([[1], [2], [3]])  # Should create a 3-by-1 matrix.


def test_dim():
    A = Matrix(4, 3)
    print(f'A.numRows() = {A.numRows()}')
    print(f'A.numCols() = {A.numCols()}')

    B = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print(f'B.numRows() = {B.numRows()}')
    print(f'B.numCols() = {B.numCols()}')

    C = Matrix([[1, 2, 3]])
    print(f'C.numRows() = {C.numRows()}')
    print(f'C.numCols() = {C.numCols()}')

    D = Matrix([[1], [2], [3]])
    print(f'D.numRows() = {D.numRows()}')
    print(f'D.numCols() = {D.numCols()}')


def test_getset():
    A = Matrix(2, 4)
    A[0, 0] = 1
    A[0, 1] = 2
    A[0, 2] = 3
    A[0, 3] = 4
    A[1, 0] = 5
    A[1, 1] = 6
    A[1, 2] = 7
    A[1, 3] = 8
    print(A)  # This calls __str__ which in turn queries individual matrix entries.


def test_swaps():
    A = Matrix([
        [1, 2, 3],
        [10, 11, 12],
        [7, 8, 9],
        [4, 5, 6]
    ])
    A.swapRows(1, 3)
    print(A)

    B = Matrix([
        [1, 2, 4, 3],
        [5, 6, 8, 7],
        [9, 10, 12, 11]
    ])
    B.swapCols(2, 3)
    print(B)


def test_add():
    A = Matrix([
        [1, 2],
        [3, 4],
        [5, 6]
    ])
    B = Matrix([
        [-2, -1],
        [-4, -3],
        [-6, -5]
    ])
    C = A + B
    print(C)


def test_mul():
    A = Matrix([
        [1, 2],
        [3, 4],
        [5, 6]
    ])
    B = Matrix([
        [1, 0, 0, -1, 0],
        [0, 1, 2, +1, 0]
    ])
    C = A * B
    print(C)


def test_eq():
    A = Matrix([
        [1, 2],
        [3, 4]
    ])
    B = Matrix(2, 2)
    B[0, 0] = 1
    B[0, 1] = 2
    B[1, 0] = 3
    B[1, 1] = 4
    print(A == B)


if __name__ == '__main__':
     test_init()
     test_dim()
     test_getset()
     test_swaps()
     test_add()
     test_mul()
     test_eq()
