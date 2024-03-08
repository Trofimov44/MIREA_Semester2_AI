import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

url = "https://raw.githubusercontent.com/akmand/datasets/master/iris.csv"
df = pd.read_csv(url)
df['sepal_length_cm_normalized'] = MinMaxScaler().fit_transform(df[['sepal_length_cm']])
df['sepal_width_cm_standardized'] = StandardScaler().fit_transform(df[['sepal_width_cm']])
print(df.head())


