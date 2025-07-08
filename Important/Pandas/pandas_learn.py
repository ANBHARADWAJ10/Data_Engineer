import pandas as pd

# python-db-learning/Important/Pandas/StudentsPerformance.csv
df = pd.read_excel('StudentsPerformance.xlsx')
# print(df.iloc[67])

# print(df.head(2))
# print(df.tail(2))
# print(df.sample(5)) # view random rows
# print(df.shape)
# print(df.info())
# print(df.describe())
# print(df.dtypes)
# print(df.columns)
# print(df.index)

# print(df['math score'])
# print(df[['math score', 'reading score']])
# print(df.iloc[0])
# print(df.loc[0])
# print(df.iloc[1:4])
# print(df.loc[1:4])
# print(df[df['math score'] > 90])
# print(df.iloc[0:5, 0:2])
# print(df.set_index('Student ID'))