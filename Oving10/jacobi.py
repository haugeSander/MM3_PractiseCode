from sympy import *

A = Matrix([5.0, 2.0, 3.0], [3.0, 6.0, -2.0], [-1.0, 3.0, 5.0])

D = diag(A)
print(D)
