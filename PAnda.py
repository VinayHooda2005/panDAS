import pandas as pd 
data={
    'Subject':['Math','Science','English'],
    'Marks':[85,90,78]
}
df=pd.DataFrame(data,index=['S1','S2','S3'])
print(df)
print("==================")

#Access data using loc and iloc

print(df.loc['S1'])
print("==================")

print(df.iloc[-1])
print("==================")

#add new column

import pandas as pd 
data={
    'Subject':['Math','Science','English'],
    'Marks':[85,90,78]
}
df=pd.DataFrame(data,index=['S1','S2','S3'])
df['Grade']=['B','A','C']
print(df)
print("===================")

#add new row
new_data=pd.DataFrame([{'Subject':'History','Marks':88,'Grade':'A'}],index=['S4'])
df=pd.concat([df,new_data])
print(df)
print("===================")

#add multiple new row
new_data=pd.DataFrame([{'Subject':'Geography','Marks':'70','Grade':'B'},{'Subject':'Computer',
                    'Marks':'95','Grade':'A'}],index=['S5','S6'])
df=pd.concat([df,new_data])
print(df)
