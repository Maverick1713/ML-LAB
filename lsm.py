import numpy as np 
X = np.array([[0.2,0.4],[0.4,0.6],[0.6,0.8]])
y_true = np.array([0,1,1])
y_true[0]= 1.5
X_b = np.c_[np.ones((X.shape[0],1)),X]
intial_weights = np.random.randn(X_b.shape[1],1)
learning_rate = 0.01
n_interations = 1000
weights = intial_weights.copy()
for _ in range(n_interations):
    errors = y_true-X_b.dot(weights).flatten()
    gradients = -X_b.dot(errors.reshape(-1,1))
    print(errors.shape)
    weights = weights - learning_rate*gradients
print("intial_weights:")
print(intial_weights)
print("\n Error")
print(errors)
print("\n Updated Weights: ")
print(weights)