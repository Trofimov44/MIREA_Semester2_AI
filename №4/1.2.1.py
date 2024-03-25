import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from numpy import *
from numpy.random import *
from pandas import DataFrame, Series
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

u = "https://raw.githubusercontent.com/AnnaShestova/salary-years-simple-linear-regression/master/Salary_Data.csv"
dataset = pd.read_csv(u)

print(dataset.shape)
dataset.describe()

plt.scatter(dataset['YearsExperience'],dataset["Salary"],color = 'r',label = "Salary data ")
plt.xlabel("YearsExperience")
plt.ylabel("Salary")
plt.show()


x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values
print(x)
print(y)

X_train, X_test, y_train, y_test = train_test_split(x, y, train_size = 0.2, random_state = 0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.intercept_)
print(regressor.coef_)


y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, "Predicted": y_pred})

df.plot(kind = 'bar')
plt.grid(which='major', linestyle = '-', linewidth ='0.5', color = 'green')
plt.grid(which='minor', linestyle = ':', linewidth ='0.5', color = 'black')
plt.show()

plt.scatter(X_test,y_test,color = 'gray')
plt.plot(X_test,y_pred,color = 'red', linewidth=2)
plt.show()
