import numpy as np

def LUfactorize(A):
   n,m = np.shape(A)
   L = np.eye(n)
   U = np.zeros((n,n))
   U = A.copy()
   for j in range(n - 1):
      if (U[j, j] == 0):  # 0 i pivot element
         raise np.linalg.LinAlgError("Zero pivot encountered")
         return

      for i in range(j + 1, n):
         mult = U[i, j] / U[j, j]
         L[i,j] = mult
         U[i,j:] -= mult * U[j, j:]

   return L,U


# Resten av koden kan du la stå som den er :)
A = np.array([1.0, 2, -1, 0, 3, 1, 2, -1, 1]) #Prøv å skrive "1.0" som "1" - Hva foregår?
A = A.reshape((3, 3))

try:
   L,U = LUfactorize(A)
   print(L)
   print(U)
except np.linalg.LinAlgError as e:
   print(f"LinAlgError: {e}")
