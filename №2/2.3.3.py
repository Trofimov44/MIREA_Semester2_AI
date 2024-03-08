import pandas as pd  
u = "https://github.com/akmand/datasets/blob/main/cdc.csv" 
dataframe=pd.read_csv(u) 
dataframe.head(10) 
dataframe.tail(3)  
dataframe.shape  
dataframe.describe()  
dataframe.iloc[1:4]  
dataframe[dataframe[''] == ''].head(5)

