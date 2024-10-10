import numpy as np
import matplotlib.pyplot as plt

start= 0
end= 10
impulse= 3
dt_seq= np.arange(start, end+1)

print(f"Start: {start}, End: {end}, impulse: {impulse}")
print("Sequence length: ", end-start)
print("Discrete-time sequence: {}", format(dt_seq))

unit_sample_list= [1 if i== impulse else 0 for i in range(end+1)]
unit_sample_array= np.array(unit_sample_list)

print(f"Unit sample sequence: {unit_sample_array}")