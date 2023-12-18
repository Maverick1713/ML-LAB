import numpy as np
import pandas as pd
from collections import Counter
import math
def euclidean(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
def predict(new,k,data):
    dist=[]
    for point in data:
        dist.append((list(point),euclidean(list(point)[:2],new)))
    print("dist: " , dist)
    dist.sort(key=lambda x:x[1])
    nb=[point[0][2] for point in dist[:k]]
    pred=Counter(nb).most_common(1)[0][0]
    print(pred)
    return pred
K=10
data=pd.DataFrame({'x':[np.random.randint(1,31) for x in range(30)],'y':[np.random.randint(1,31) for y in range(30)],'label':[np.random.randint(1,3) for _ in range(30)]})
data_values=data.values.tolist()
print(data_values)
new=list(map(int,input("Data Point: ").split()))
print(new)
pred=predict(new,K,data_values)
print("Predicted label for {}: {}".format(new,pred))
