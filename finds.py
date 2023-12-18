import pandas as pd 
import numpy as np 

data = pd.read_csv('es.csv')
d = np.array(data)[:,:-1]
print("The Attributes are : \n", d)
target = np.array(data)[:,-1]
print("The target is : \n",target)

def finds(d,t):
    for i,val in enumerate(t):
        if val== "yes":
            sh = d[i].copy()
            break
    for i,val in enumerate(d):
        if t[i] == "yes":
            for x in range(len(sh)):
                if sh[x]!=val[x]:
                    sh[x]= "?"
    return sh
print("The specific Hypothesis is : ",finds(d,target))
