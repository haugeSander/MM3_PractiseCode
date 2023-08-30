import numpy as np

def nest(c,x):
    y = c[-1]
    for i in range(len(c) - 2, -1, -1):
        y = y * x + c[i]
    return y

#Denne funksjonen skal printe ut feilen du får når du bruker funksjonen "funk(c,x)"
#til å evaluere polynomet fra oppgaveteksten ved å sammenligne det med det ekvivalente uttrykket
def test_feil(funk):
    c = np.ones(51)
    x = 1.00001
    Px = (x ** 51 - 1) / (x - 1)
    error = abs(Px - funk(c, x))
    error = round(error, 13 - (int(np.log10(abs(error))) + 1))
    return "{:.11e}".format(error)