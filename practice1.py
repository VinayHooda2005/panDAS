import pandas as pd

# Create a DataFrame
data={
    "Name":['Rahul','Priya','Aman'],
    "Marks":[85,90,78]

}
df=pd.DataFrame(data)
print(df)
print("==============")

#Complete information about DataFrame
df=df.info()
print(df)
print("============")

# display statistical summary
data={
    "Name":['Rahul','Priya','Aman'],
    "Marks":[85,90,78]

}
df=pd.DataFrame(data)
print(df)
print("==============")
print(df.describe())


