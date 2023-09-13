import numpy as np

def trapes(f, g, y1_init, y2_init, h, t_slutt):
   t = np.arange(0, t_slutt+h, h)
   y1 = np.zeros_like(t)
   y2 = np.zeros_like(t)
   y1[0] = y1_init
   y2[0] = y2_init

   for i in range(1,t.size):
       a = f(y1[i-1], y2[i-1])
       b = g(y1[i-1], y2[i-1])
       c = f(y1[i-1]+h*a, y2[i-1]+h*b)
       d = g(y1[i-1]+h*a, y2[i-1]+h*b)
       y1[i] = y1[i-1] + (h/2)*(a+c)
       y2[i] = y2[i-1] + (h/2)*(b+d)
   return t, y1, y2

f = lambda y1,y2: y2+y1
g = lambda y1,y2: y2-y1
t, y1, y2 = trapes(f, g, 1, 0, 0.25, 1.0)

print(y1)
print(y2)

#headers = ["t", "trapes", "error"]
#print(f"{headers[0]:<8}{headers[1]:<8} {headers[2]:<8}")
#for i in range(t.size):
#   print(f"{t[i]:<8.2f}{y[i]:<8.3f}{error[i]:<8.3f}")