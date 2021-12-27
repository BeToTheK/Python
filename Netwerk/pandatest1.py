from pandas import DataFrame, read_csv

import random
import matplotlib.pyplot as plt
import pandas as pd 
import matplotlib 
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

random.seed(500)

random_names = [names[random.randint(0,4)] for i in range(1000)]
random_births = [random.randint(0,1000) for i in range(1000)]

bigdata = list(zip(random_names,random_births))
# print(bigdata)

df = pd.DataFrame(bigdata,columns=['Names','Births'])
# print(df['Names'].describe())
# print(df['Names'].count())

name = df.groupby('Names')
df = name.sum()
# print(df)

Sorted = df.sort_values(['Births'], ascending=False)
# print(Sorted.head())

df['Births'].plot.bar()
plt.show()