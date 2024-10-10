import numpy as np
import matplotlib.pyplot as plt

n= np.linspace(0, 4*np.pi, 64)
amp= 3
omega= 3*np.pi/8
phase= np.pi/2
xn=amp* np.cos(omega+n + phase)

plt.figure(figsize= (10,5))

plt.stem(n, xn, basefmt= "blue"); plt.grid()

plt.title("Periodic sequence")
plt.xlabel("n"); plt.ylabel("x[n]")

plt.show()