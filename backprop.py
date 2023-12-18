import numpy as np
import matplotlib.pyplot as plt

def sigmoid(a):
    return 1/(1+np.exp(-1*a))
def error(predicted,target):
    return np.power(predicted-target,2)
def error_predicted_deriv(predicted,target):
    return 2*(predicted-target)
def sigmoid_act_deriv(a):
    return sigmoid(a)*(1-sigmoid(a))
def act_w_deriv(x): 
    return x
def update_w(w,grad,learning_rate):
    return w-learning_rate*grad

x1=0.1
x2=0.4
target = 0.7
learning_rate = 0.01
w1 = np.random.rand()
w2 = np.random.rand()
print("Initial Weights = ",w1,w2)
predicted_output = []
network_error = []
weight1,weight2 = [], []
old_err = 0
for k in range(80000):
    y = w1*x1+w2*x2
    predicted = sigmoid(y)
    err = error(predicted,target)
    predicted_output.append(predicted)
    network_error.append(err)
    weight1.append(w1)
    weight2.append(w2)
    g1=error_predicted_deriv(predicted,target)
    g2 = sigmoid_act_deriv(y)
    g3w1 = act_w_deriv(x1)
    g3w2 = act_w_deriv(x2)
    gradw1 = g3w1*g2*g1
    gradw2 = g3w2*g2*g1
    w1 = update_w(w1 , gradw1 , learning_rate)
    w2 = update_w(w2,gradw2,learning_rate)

plt.figure()
plt.plot(network_error)
plt.title("Iteration Number vs Error")
plt.xlabel("Iteration Number")
plt.ylabel("Error")
plt.savefig('error.png')
plt.show()

plt.figure()
plt.plot(predicted_output)
plt.title("Iteration Number vs Prediction")
plt.xlabel("Iteration Number")
plt.ylabel("Prediction")
plt.savefig('pred.png')
plt.show()


plt.figure()
plt.plot(weight1)
plt.title("Iteration Number vs Weight1")
plt.xlabel("Iteration Number")
plt.ylabel("Weight1")
plt.savefig('w1.png')
plt.show()


plt.figure()
plt.plot(weight2)
plt.title("Iteration Number vs Weight2")
plt.xlabel("Iteration Number")
plt.ylabel("Weight2")
plt.savefig('w2.png')
plt.show()