import pandas as pd
df=pd.read_csv('Students_Data.csv')
print(df['Age'])
print("===============")

print(df[['Student Name','Marks']])
print("================")

import pandas as pd
df=pd.read_csv('pokemon_list.csv')
print(df.to_string())
print("=======================")

import pandas as pd
df=pd.read_csv('pokemon_list.csv',index_col='NAME')
print(df.loc['Squirtle'])
print(df.loc['Blastoise',['WEIGHT (KG)']])
print("==============")

print(df.iloc[0:21:3])