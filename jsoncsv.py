# Importing data (CSV/JSON) & Selection 

# import csv file
import pandas as pd
df=pd.read_csv('Students_Data.csv')
print(df.to_string())
print("================================")


# import json file
import pandas as pd
df=pd.read_json('Students_Data.json')
print(df.to_string())
print("================================")


# selection by single column
import pandas as pd
df=pd.read_csv('Students_Data.csv')
print(df['Student Name'].to_string())
print("================================")

# Selection by multiple columns
import pandas as pd
df=pd.read_json('Students_Data.json') 
print(df[['Student Name','Age']].to_string())
print("================================")

# Selection by Row-loc & iloc

# df.loc[0]-by default numeric index
import pandas as pd
df=pd.read_json('Students_Data.json')
print(df.loc[0])
print("================================")

#custom index +loc by label
df=pd.read_csv('Students_Data.csv', index_col='Student Name')
print(df.loc['Rohan Gupta'])
print("================================")


#loc row label + specific column
import pandas as pd
df=pd.read_csv('Students_Data.csv', index_col='Student Name')
print(df.loc['Rohan Gupta', ['Age', 'Marks']])
print("================================")

# iloc --slicing row by index
import pandas as pd
df=pd.read_csv('Students_Data.csv')
print(df.iloc[0:3])
print("================================")

# iloc -- step + column slice
import pandas as pd
df=pd.read_csv('Students_Data.csv')
print(df.iloc[0:5:2, 0:2])
print("================================")