import numpy as np
import matplotlib.pyplot as plt

n=np.arange(30)
xn= np.power(0.5,n)

def DTFT(xk, k,T= 1000):
    omega= np.linspace(-np.pi, np.pi, T)
    X= np.zeros(T, dtype="complex64")
    for idx, val in enumerate(k):
        X+= xk[idx]*np.exp(-1j *omega*val)
    return X, omega

X,omega= DTFT(xn,n)

magnitude_X= np.abs(X)
phase_X= np.angle(X, deg="True")

plt.figure(figsize=(15,10))
plt.subplot(3,1,1)
plt.stem(n,xn, basefmt="blue")
plt.grid()
plt.xlabel("n")
plt.ylabel("x[n]")

plt.subplot(3,1,2)
plt.plot(omega, magnitude_X)
plt.grid()
plt.xlabel("omega")
plt.ylabel("Magnitude of X")

plt.subplot(3,1,3)
plt.plot(omega, phase_X)
plt.grid()
plt.xlabel("omega")
plt.ylabel("Phase of X")

plt.show()