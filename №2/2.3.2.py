import pandas as pd
url = "https://raw.githubusercontent.com/akmand/datasets/master/iris.csv."
x = pd.read_csv(url)
print(x.head())
