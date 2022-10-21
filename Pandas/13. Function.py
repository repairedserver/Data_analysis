import pandas as pd
df = pd.read_csv('people.csv')
print(df)
df['학교'] = df['학교'] + "고등학교"
print(df)

def addCm(height):
    return str(height) + 'cm'
df['키'] = df['키'].apply(addCm)
print(df)