import pandas as pd

# creating a DataFrame from a dictionary
data={
    "Name":["Sawan","Vinay","Jatin","Sahil","Mohit"],
    "Class":["Python","Sql","HTML","Python","Sql"],
    "Roll No":["201","202","203","204","205"],
    "Marks":[85,70,88,76,90]
    }
df=pd.DataFrame(data)
print(df)
print("===============")

# diplaying the first 3 rows of the DataFrame
print(df.head(3))
print("===============")

# display last 2 rows of the DataFrame
print(df.tail(2))
print("===============")

# displaying the column 'Marks' of the DataFrame
print(df["Marks"])
print("==============")

# displaying the columns 'Marks' and 'Name' of the DataFrame
print(df[["Marks","Name"]])
print("==============")

# display second row using loc
df=pd.DataFrame(data,index=['a','b','c','d','e'])
print(df.loc['b'])
print("==============")

# display third row using iloc
print(df.iloc[2])
print("==============")

# find the shape of the DataFrame
print(df.shape)
print("==============")

# Display the column names of the DataFrame
print(df.columns)
print("==============")

# Display the data types of each column in the DataFrame
print(df.dtypes)
print("==============")

# sort marks in descending
df=df.sort_values("Marks",ascending=False)
print(df)
print("==============")

# add new column named city 
df["City"]=['Rohtak','Rohtak','Gohana','Sonipat','Panipat']
print(df)
print("==============")

# remove the column city
df=df.drop("City",axis=1)
print(df)
print("==============")

# dataframe with missing values
data={
    "Name":["Sawan","Vinay","Jatin","Sahil","Mohit"],
    "Marks":[85,None,88,None,90],
    "Roll No":["201",None,"203","204","205"]
}
df=pd.DataFrame(data)
print(df)
print("==============")

# replace missing values with 100
data={
    "Name":["Sawan","Vinay","Jatin","Sahil","Mohit"],
    "Marks":[85,None,88,None,90],
    "Roll No":["201",None,"203","204","205"]
}
df=pd.DataFrame(data)
df=df.fillna(100)
print(df)
print("==============")

# remove row with missing value
data={
    "Name":["Sawan","Vinay","Jatin","Sahil","Mohit"],
    "Marks":[85,None,88,None,90],
    "Roll No":["201",None,"203","204","205"]
}
df=pd.DataFrame(data)
df=df.dropna()
print(df)
print("==============")

# convert all names to lowercase
df["Name"]=df["Name"].str.lower()
print(df)
print("==============")

# filter students with marks
result=df[df["Marks"]>80]
print(result)
print("==============")

# save the dataframe as an excel file
data={
    "Name":["Sawan","Vinay","Jatin","Sahil","Mohit"],
    "Class":["Python","Sql","HTML","Python","Sql"],
    "Roll No":["201","202","203","204","205"],
    "Marks":[85,70,88,76,90]
    }
df=pd.DataFrame(data)
df.to_excel('Students_Data.xlsx',index=False)
print("Excel file created successfully.")
print("===============")