import numpy as np
import matplotlib.pyplot as plt

start=0
end=20
impulse= 3
dt_seq= np.arange(start, end+1)

unit_sample_list= [1 if i== impulse else 0 for i in range(end+1)]
unit_sample_array= np.array(unit_sample_list)

plt.figure(figsize= (10,5))
plt.stem(dt_seq, unit_sample_array); plt.grid()
plt.title("Unit sample sequence")
plt.xlabel("n"); plt.ylabel("x[n]")

plt.show()