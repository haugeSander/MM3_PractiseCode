import numpy as np


def fikspunkt_solve(f, x0, tol):
    x = x0

    for i in range(8):
        x = f(x)
        print(x)

        if abs(x - x0) < tol:
            return x
        x0 = x

    return x


f1 = lambda x: x ** 3 - 2 * x - 2  # Hvilken funksjon skal inn i fikspunkt_solve? (lign. 1)
f2 = lambda x: np.exp(x) + x - 7  # Hvilken funksjon skal inn i fikspunkt_solve? (lign. 2)
f3 = lambda x: np.exp(x) + np.sin(x) - 4  # Hvilken funksjon skal inn i fikspunkt_solve? (lign. 3)
funcs = [f1, f2, f3]
maks_feil = 1 * 10 ** (-6)  # ????
expected_sols = [1.5, 1.5, 1]
sols = []
iteration = 0

for f in funcs:
    x_sol = fikspunkt_solve(f, 1, maks_feil)
    sols.append(x_sol)
    iteration += 1

print(f"Løsning til første ligning x = {sols[0]}")
print(f"Løsning til andre ligning x = {sols[1]}")
print(f"Løsning til tredje ligning x = {sols[2]}")