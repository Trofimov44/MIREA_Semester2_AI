import pandas as pd
url = "https://raw.githubusercontent.com/akmand/datasets/master/iris.csv"
df = pd.read_csv(url)
print(df.head(6))
