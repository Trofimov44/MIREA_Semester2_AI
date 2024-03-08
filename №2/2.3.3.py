import pandas as pd  
u = "" 
dataframe=pd.read_csv(u) 
dataframe.head(10) 
dataframe.tail(3)  
dataframe.shape  
dataframe.describe()  
dataframe.iloc[1:4]  
dataframe[dataframe['species'] == 'setosa'].head()
