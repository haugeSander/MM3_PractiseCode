import numpy as np

def euler(f, y_init, h, t_slutt):
   t = np.arange(0, t_slutt+h, h)
   y = np.zeros_like(t)
   y[0] = y_init

   for i in range(1,t.size):
      y[i] = y[i-1]+h*f(t[i-1])
      t[i] = t[i-1] + h
   return t, y

f = lambda t: t
y_exact = lambda t: (1/2) * t**2 + 1
t, y = euler(f, 1, 0.25, 1.0)
# Creates a list of actual values.
y_exact_list = [y_exact(t_i) for t_i in t]
# Extracts exact value from all places in array.
error = abs(np.array(y)-np.array(y_exact_list))

headers = ["t", "euler", "error"]
print(f"{headers[0]:<8}{headers[1]:<8} {headers[2]:<8}")
for i in range(t.size):
   print(f"{t[i]:<8.2f}{y[i]:<8.3f}{error[i]:<8.3f}")