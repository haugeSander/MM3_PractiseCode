import numpy as np

#---------> Kod i vei

def newton(f, df, x0, tol):
    xn = x0
    iteration = 0

    while iteration < 30:
        xn = x0 - (f(x0)/df(x0))
        print(xn)
        x0 = xn

        iteration += 1

        if xn-x0 < tol:
            return xn

    return xn

fx = lambda r: 4*np.pi*r**3+20*np.pi*r**2-360
dfx = lambda r: 12*np.pi*r**2+40*np.pi*r

tol = 1*10^(-4)

#<--------------
radius = newton(fx, dfx, 5, tol) #La variabelen radius holde svaret ditt