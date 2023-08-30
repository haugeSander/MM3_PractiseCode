import numpy as np

def task11():
   a = 3344556600.0
   b = 1.2222222
   c = np.sqrt(a ** 2 + b ** 2)

   Px = (c ** 51 - 1) / (c - 1)
   error = abs(Px - c)
   #error = round(error, 13 - (int(np.log10(abs(error))) + 1))

   print("a:", a)
   print("c:", c)
   print("Diff:", error)