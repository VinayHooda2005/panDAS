import pandas as pd

                    #creating series in pandas
data=[10,20,30,40]
series=pd.Series(data)
print(series)

                    #series with float values
data=[10.2,20.5,30.4,40.6]
series=pd.Series(data)
print(series)

                    #series with string values
data=['A','B','C']
series=pd.Series(data)
print(series)

                    #series with boolean
data=['True','False','True']
series=pd.Series(data)
print(series)

                    #index in series
data=[10,20,30,40]
series=pd.Series(data,index=['a','b','c','d'])
print(series)

                    #hide index
data=[10,20,30,40]
series=pd.Series(data)
print(series.to_string(index=False))

                    #loc in pandas for location with label        
data=[10,20,30,40]
series=pd.Series(data,index=['a','b','c','d'])
print(series.loc['a'])

                    #changes in data with loc
data=[10,20,30,40]
series=pd.Series(data,index=['a','b','c','d'])
series.loc['a']=50
print(series)

                    #update data with loc
data=[10,20,30,40]
series=pd.Series(data,index=['a','b','c','d'])
series.loc['a']+=50
print(series) 

                    #iloc in pandas for location with integer
data=[10,20,30,40]
series=pd.Series(data,index=['a','b','c','d'])
print(series.iloc[1])

                    #changes with iloc
data=[10,20,30,40]
series=pd.Series(data)
series.iloc[1]=50
print(series)

                    #update data with loc
data=[10,20,30,40]
series=pd.Series(data)
series.iloc[1]+=50
print(series)

                    #series in dictionary
calories={
    'Day 1':1750,
    'Day 2':2000,
    'Day 3':2100
    }
series=pd.Series(calories)
print(series)

                    #filtering in series
data=[200,250,300,400]
series=pd.Series(data)
print(series[series<=250])

calories={
    'Day 1':1750,
    'Day 2':2000,
    'Day 3':2100
    }
series=pd.Series(calories)
print(series[series<=2000])


