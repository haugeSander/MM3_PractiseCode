import numpy as np


def LUfactorize(A):
    n, m = np.shape(A)
    L = np.eye(n)
    U = np.zeros((n, n))
    U = A.copy()
    for j in range(n - 1):
        if (U[j, j] == 0):  # 0 i pivot element
            raise np.linalg.LinAlgError("Zero pivot encountered")

        for i in range(j + 1, n):
            mult = U[i, j] / U[j, j]
            L[i, j] = mult
            U[i, j:] -= mult * U[j, j:]

    return L, U

def LUsolve(L, U, b):
    c = np.zeros_like(b)
    n = len(c)
    for i in range(n - 1, -1, -1):
        c[i] = b[i]
        for j in range(i + 1, n):
            c[i] = c[i] - ??????

    x = c.copy()

    for i in ?????:
        for j in ??????:
            x[i] = ?????
        x[i] = ?????

    return x

A = np.array([[3, 1, 2], [6, 3, 4], [3, 1, 5]])
b = np.array([0, 1, 3]).T

try:
    L, U = LUfactorize(A)
    x = LUsolve(L, U, b)
except np.linalg.LinAlgError as e:
    print(f"LinAlgError: {e}")

