from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import metrics
data = pd.read_csv('iris.csv')
x = data.iloc[:,1:-1]
y = data.iloc[:,-1]
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train,Y_train)
print(knn.predict(X_test))
y_pred = knn.predict(X_test)
print("The accuracy is  :",metrics.accuracy_score(Y_test,y_pred))
new_data_point = [[6.0, 2.0, 4.8, 1.8]]
predicted_class = knn.predict(new_data_point)
print("The predicted class for the point {new_data_point[0]} is: {predicted_class[0]}")