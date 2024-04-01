import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
target = [0, 0, 0, 1, 1, 1]
from sklearn import tree
classifier=tree.DecisionTreeClassifier()  
classifier.fit(X,target)
tree.plot_tree(classifier)
