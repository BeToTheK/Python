import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import networkx
from bokeh.io import output_notebook, show, save
output_notebook()

# df = pd.read_csv('suckas.csv')
pd.set_option('display.max_columns',6)
# df = pd.DataFrame(df,columns=['Name','Net worth','Age','Nationality','Source of wealth'])
# df1 = pd.read_csv('suckas20.csv')
# df1 = pd.DataFrame(df1,columns=['Name','Net worth','Age','Nationality','Source of wealth'])
# df2 = pd.read_csv('suckas19.csv')
# df2 = pd.DataFrame(df2,columns=['Name','Net worth','Age','Nationality','Source of wealth'])
# df3 = pd.read_csv('suckas18.csv')
# df3 = pd.DataFrame(df3,columns=['Name','Net worth','Age','Nationality','Source of wealth'])
# df4 = pd.read_csv('suckas17.csv')
# df4 = pd.DataFrame(df4,columns=['Name','Net worth','Age','Nationality','Source of wealth'])

# #Sorted = df.sort_values(['Net worth'],ascending=False)
# # print("Who is the biggest sucka of them all?")
# frames = [df,df1,df2,df3,df4]

# result = pd.concat(frames)
# grp = result.groupby(["Nationality"])["Name"].count()
# # grp.plot.bar(title='Mean income of top 10 mills 2020-21')

#result.to_csv('suckas18-21.csv')# print(df[['Name','Net worth','Nationality']])
# df.plot(x ='Name', y='Net worth', kind = 'bar')

# df1.plot(x ='Name', y='Net worth', kind = 'bar')
# plt.show()

#################################################################
#### Merged DF ######################

data = pd.read_csv('suckas18-21.csv')
df = pd.DataFrame(data,columns=['Name','Net worth','Age','Nationality','Source of wealth'])
# df.plot(x ='Name', y='Net worth', kind = 'bar')
# orderdf = df.sort_values('Net worth',ascending=False)
G = networkx.from_pandas_edgelist(df, 'Nationality', 'Name', 'Source of wealth')


# print(orderdf)
# grp = orderdf.groupby(["Name"])['Net worth'].mean()
# grp.plot.bar()
# plt.show()









