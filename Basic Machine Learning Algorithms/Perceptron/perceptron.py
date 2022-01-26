import numpy as np
import matplotlib.pyplot as plt

ip_features = np.array([[0,0],[0,1],[1,0],[1,1]])
print("Input Shape: ",ip_features.shape)
print("Input Features: ",ip_features)

target_op = np.array([[0,1,1,1]])
target_op = target_op.reshape(4,1)
print("Target output shape: ",target_op.shape)
print("Taget Output: ",target_op)

weights = np.array([[0.1],[0.2]])
print("Weights Shape: ",weights.shape)
print("Weights: ",weights)

bias = 0.3
lr = 0.05

def sigmoid(x):
    return 1/(1+np.exp(-x))

def derivative_sigmoid(x):
    return (sigmoid(x) * (1- sigmoid(x)))

error = []
r = [i for i in range(5000)]

for epochs in range(5000):
    ip = ip_features
    in_o = np.dot(ip,weights)+bias
    out_o = sigmoid(in_o)

    err = out_o - target_op

    x = err.sum()
    error.append(x)
    print(x)

    derr_outo = err
    douto_dino = derivative_sigmoid(out_o)

    d = derr_outo * douto_dino

    ip = ip_features.T
    d_final = np.dot(ip,d)

    weights = (weights - (lr * d_final))

    for i in d:
        bias = (bias - (lr * i))

single_point = np.array([1,0]) 
result1 = np.dot(single_point, weights) + bias 
result2 = sigmoid(result1)
print(result2) 
single_point = np.array([1,1]) 
result1 = np.dot(single_point, weights) + bias 
result2 = sigmoid(result1)
print(result2)
single_point = np.array([0,0])
result1 = np.dot(single_point, weights) + bias 
result2 = sigmoid(result1)
print(result2)

plt.figure(dpi = 100)
plt.plot(r,error,color = 'red')
plt.grid()
plt.xlabel("Iteration")
plt.ylabel("Error")
plt.show()
