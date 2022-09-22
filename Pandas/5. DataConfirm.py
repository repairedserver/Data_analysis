import pandas as pd
df = pd.read_csv('people.csv', index_col='이름')
print(df)

print(df.describe())