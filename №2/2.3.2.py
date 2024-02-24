import pandas as pd
url = "https://github.com/akmand/datasets/blob/996c328034dd22d7f6a6df64e45ea8debce7aacf/arrhythmia.csv"
x = pd.read_csv(url)
print(x.head())
