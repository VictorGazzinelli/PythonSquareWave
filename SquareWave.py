import numpy as np
import matplotlib.pyplot as plt

def fourierSquareTransform (infinity, x):
  sum = 0
  for i in range (1,infinity):
    k = 2*i -1
    sum += ((1/k)*(np.sin(k * np.pi * x)))
  return (4/np.pi) * sum;

# First Graph Vars
x1 = np.arange(0.0, 5.0, 0.01)
y1 = (2.5) + (2.5 * np.sin(2 * np.pi * x1)) 

# Second Graph Vars
x2 = np.linspace(0.0, 5.0)
y2 = (2.5) + (2.5 * fourierSquareTransform(2**16,x2) ) # 64k Codec

plt.subplot(2, 1, 1)
plt.plot(x1, y1)
plt.title('Analog Wave x Digital Wave')
plt.ylabel('Voltage(v)')

plt.subplot(2, 1, 2)
plt.plot(x2, y2)
plt.ylabel('Voltage (v)')
plt.xlabel('Time (s)')

plt.show()
