import pandas as pd  
url = "https://raw.githubusercontent.com/akmand/datasets/master/iris.csv"
df = pd.read_csv(url)
df.head(10) 
df.tail(3)  
df.shape  
df.describe()  
df.iloc[1:4]  
df[df['species'] == 'setosa'].head()
