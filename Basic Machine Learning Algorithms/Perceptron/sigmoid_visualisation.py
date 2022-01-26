import numpy as np
import matplotlib.pyplot as plt

ip = np.linspace(-10,10,100)

def sigmoid(x):
    val = 1 / (1 + np.exp(-x))
    return val

op = sigmoid(ip)

plt.figure(dpi = 100)
plt.plot(ip,op)
plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Sigmoid Function")
plt.grid()
plt.show()