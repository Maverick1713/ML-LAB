import pandas as pd 
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

le = preprocessing.LabelEncoder()
t = pd.read_csv('dataset.csv')
t = t.apply(le.fit_transform)
features = ['Outlook','Temperature','Humidity','Wind']
X = t[features]
y = t.PlayTennis
clf = DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X,y)
fig,axes = plt.subplots(nrows=1,ncols=1,figsize=(4,4),dpi=300)
tree.plot_tree(clf,feature_names=features,class_names=['No',"Yes"],filled=True)
fig.savefig('Tree.png')
