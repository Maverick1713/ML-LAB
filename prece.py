import numpy as np
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1])
w = np.array([0.1,0.2])
b=0.3
learn = 0.1
def activate(z,threshold):
    return 1 if z>=threshold else 0
epochs = 100
threshold = 0.5
for epoch in range(epochs):
    for i in range(len(X)):
        z = np.dot(X[i],w)+b
        prediction = activate(z,threshold)
        w+=learn*(y[i]-prediction)*X[i]
        b+=learn*(y[i]-prediction)
tests = np.array([[0,0],[0,1],[1,0],[1,1]])
for test in tests:
    z = np.dot(test,w)+b
    prediction = activate(z,threshold)
    print(f'input: {test} , prediction: {prediction}')