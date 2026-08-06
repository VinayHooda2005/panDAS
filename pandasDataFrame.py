import pandas as pd

data={
    "name":['Vinay','Jatin','Sawan'],
    "age":[21,18,22],
    "marks":[80,85,78]
}

df=pd.DataFrame(data,index=['Student 1','Student 2','Student 3'])
print(df)

                        #Accesing rows using loc and iloc
#using loc "label based indexing"
print(df.loc['Student 1'])

#using iloc "position based indexing"
print(df.iloc[1])

                            #Adding New Column
df["Job"]=['IT','HR','Sales']
print(df)

                            #Adding New Row
import pandas as pd

data={
    "name":['Vinay','Jatin','Sawan'],
    "age":[21,18,22],
    "marks":[80,85,78]
}

df=pd.DataFrame(data,index=['Student 1','Student 2','Student 3'])
new_row=pd.DataFrame([{'name':'Manish','age':18,'marks':82}],index=['Student 4'])
df=pd.concat([df,new_row])
print(df)