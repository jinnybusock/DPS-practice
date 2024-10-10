import numpy as np
import matplotlib.pyplot as plt

n= np.arange(-2,2)
xn= np.array([1,2,3,4])

plt.figure(figsize=(15,5))
plt.stem(n,xn,basefmt="blue")
plt.grid(); plt.xlabel("n"); plt.ylabel("x[n]")
plt.show()