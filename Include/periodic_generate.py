import numpy as np
import matplotlib.pyplot as plt

n= np.linspace(0, 4*np.pi, 64)
amp= 3
omega= 3*np.pi/8
phase= np.pi/2
xn=amp* np.cos(omega+n + phase)

N= 2*np.pi/ omega
print(f"Period: {N}, if k==1")