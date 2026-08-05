import pandas as pd
list=[5,10,15,20]
series=pd.Series(list)
print(series)
print("======================")

tuple=(1,2,3,4)
series=pd.Series(tuple)
print(series.iloc[1])
print("======================")

dic={ 
    "A":10,
    "B":20,
    "C":30
    }
series=pd.Series(dic)
print(series.loc['B'])
print("======================")

series.loc['C']=35
print(series)
print("======================")

print(series[series>=20])
print("======================")

data=[200,300,400,500]
series=pd.Series(data,index=['P','Q','R','S'])
print(series)
print("======================")

series.loc['Q']+=100
print(series)
print("======================")

import numpy as np
arr=np.array([10,20,30,40])
s=pd.Series(arr)
print(s.iloc[2])
