import pandas as pd

df=pd.read_excel('/home/vinoth/vinoth/Hari/ios.xls')
df=df.set_index('MPN')
finaldf = df.copy()
for i in df['WEEK'].unique():
    tempdf = df[df['WEEK']==i]
    for column in tempdf.columns:
        for indexing in tempdf.index:
            if ((indexing=='TWOS+Adj') and (pd.isnull(tempdf.at['TWOS+Adj',column]))):
                finaldf.loc[(finaldf.WEEK == i),column] = tempdf.at['TWOS',column]

print (df)
print (finaldf)












''' working

for i in df['WEEK'].unique():
    tempdf = df[df['WEEK']==i]
    for column in tempdf.columns:
        for indexing in tempdf.index:
            if ((indexing=='TWOS+Adj') and (pd.isnull(tempdf.at['TWOS+Adj',column]))):
                tempdf.at['TWOS+Adj',column] = tempdf.at['TWOS',column]


'''