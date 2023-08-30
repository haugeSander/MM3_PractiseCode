import numpy as np

def halvering_solve(f, a, b, tol):
    # Din kode her :) --->
    global c

    while (b - a) / 2 > tol:
        c = round((b + a) / 2, 8)
        print(c)

        if f(c) == 0:
            return c
        if f(c)*f(a) < 0:
            b = c
        else:
            a = c

    return c  # <---------


f = lambda x: x ** 2 - 9  # Hvilken funksjon f er det du skal finne roten av?
maks_feil = 0.0000001  # Hva blir maks feil om x_sol skal være riktig med minst 6 desimaler?
a = 2
b = 3
x_sol = halvering_solve(f, a, b, maks_feil)  # Hva må startintervallet være?
print(x_sol)
