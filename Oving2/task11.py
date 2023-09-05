import numpy as np

def naive_gauss(A,b):
    n, m = np.shape(A)
    S = np.zeros((n, n + 1))
    S[:, 0:n] = A
    S[:, -1] = b
    for j in range(n - 1):
        for i in range(j + 1, n):
            mult = S[i, j] / S[j, j]
            S[i, j] = 0.0
            for k in range(j + 1, n + 1):
                S[i, k] = S[i, k] - (mult * S[j, k])

    x = S[:, -1]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            x[i] = x[i] - S[i, j] * x[j]
        x[i] = x[i] / S[i, i]
    return x

ns = [2, 5, 10]
xs = []
for n in ns:
    H = np.zeros((n, n))

    for j in range(n):
        for i in range(n):
            H[j,i] = 1.0/(i + j + 1)

    b = np.ones(n)

    x = naive_gauss(H, b)
    xs.append(x)
    bakoverfeil = (np.max(np.abs(np.dot(H, x) - b)))  # Om du var nysgjerrig :)