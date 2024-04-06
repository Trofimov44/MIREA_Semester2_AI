import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

iris = sns.load_dataset('iris')
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)
print(model)
y_pred = model.predict(X_test)

plt.figure(figsize=(10, 7))
sns.scatterplot(x='petal_width', y='petal_length', data=iris, hue='species', s=70)
plt.xlabel("Длина лепестка, см")
plt.ylabel("Ширина лепестка, см")
plt.legend(loc=2)
plt.grid()

for i in range(len(y_test)):
    if np.array(y_test)[i] != y_pred[i]:
      plt.scatter(X_test.iloc[i, 3], X_test.iloc[i, 2], color='red', s=150)

X_train, X_test, y_train, y_test = train_test_split(
  iris.iloc[:, :-1],
  iris.iloc[:, -1],
  test_size = 0.15
)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

X_train.head()
y_train.head()

k = 10
print((f'accuracy: {accuracy_score(y_pred, y_test) :.3}'))
