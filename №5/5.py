from sklearn.model_selection import train_test_split
from sklearn import tree
import pandas as pd
import numpy as np
url="https://raw.githubusercontent.com/likarajo/petrol_consumption/master/data/petrol_consumption.csv"
dataset=pd.read_csv(url)
dataset.head()
print(dataset.shape)
dataset.describe()
from sklearn import tree
X = dataset.iloc[:, :- 1].values
y = dataset.iloc[:, 1].values
print(X)
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

regressor=tree.DecisionTreeRegressor()
regressor.fit(X_train,y_train)
tree.plot_tree(regressor)
y_pred=regressor.predict(X_test)
df=pd.DataFrame({'Реальные':y_test, 'Предсказанные':y_pred})
df
from sklearn import metrics
print('MSE:', metrics.mean_squared_error(y_test, y_pred))
print('MAE:', metrics.mean_absolute_error(y_test, y_pred))
print("MAE%:",metrics.mean_absolute_error(y_test, y_pred) / np.average(y) * 100,"%")
