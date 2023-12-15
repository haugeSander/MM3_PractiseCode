import numpy as np
#import matplotlib.pyplot as plt


def getNAK_System(x_coords, y_coords):
    n = x_coords.size  # Antall punkter
    delta = np.array([x_coords[i] - x_coords[i - 1] for i in range(1, n)])
    BigDelta = np.array([y_coords[i] - y_coords[i - 1] for i in range(1, n)])
    A = np.zeros((n, n))

    mainDiag = np.ones(n)
    mainDiag[-1] = -1
    mainDiag[1:-1] = np.array([2 * (delta[i] + delta[i-1]) for i in range(n - 2)])

    upperDiag = np.array([delta[i] for i in range(n - 1)])
    upperDiag[0] = -1
    lowerDiag = np.array([delta[i] for i in range(n - 1)])
    lowerDiag[-1] = 1

    np.fill_diagonal(A, mainDiag)
    np.fill_diagonal(A[:-1, 1:], upperDiag)
    np.fill_diagonal(A[1:, :-1], lowerDiag)

    b = np.zeros(n)
    b[1:-1] = np.array([3 * (BigDelta[i] / delta[i] - BigDelta[i - 1] / delta[i - 1]) for i in range(1, n - 1)])

    return A, b


x = np.array([1, 2, 4, 5., 7, 9])
y = np.array([2, 1, 4, 3., 0, 2])
A, bs = getNAK_System(x, y)

print(A)