import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
df = pd.read_csv('sales.csv')
X= df['X'].values.reshape(-1,1)
y=df['y'].values
model = LinearRegression()
model.fit(X,y)
y_pred = model.predict(X)
plt.scatter(X,y,color='black',label='Actual Data')
plt.plot(X,y_pred,color='blue',linewidth=3,label='Linear Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Example with Custom Dataset')
plt.legend()
plt.savefig('LinearReg.png')
plt.show()
a=model.intercept_
b=model.coef_[0]
print(f'Estimated Parameters: a = {a} , b={b}')
x_test = np.array([2.4,1.25]).reshape(-1,1)
y_pred_new = model.predict(x_test)
print(f'Predicted sales for the testing data : {y_pred_new}')