import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
%matplotlib inline
%run utilities.ipynb

input_file="data_decision_trees.txt"
data=np.loadtxt(input_file,delimiter=",")
X, y=data[:,:-1],data[:,-1]
class_0=np.array(X[y==0])
class_1=np.array(X[y==1])

