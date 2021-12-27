# import pandas as pd
# import matplotlib.pyplot as plt

# broken_df = pd.read_csv('bikes.csv')
# # Look at the first 3 rows
# #print(broken_df[:3])

# fixed_df = pd.read_csv('bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
# pd.set_option('display.max_columns', None)
# fixed_df.plot()
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

weather_2012_final = pd.read_csv('weather_2012.csv', index_col='Date/Time')
weather_2012_final['Temp (C)'].plot(figsize=(15, 6))
plt.show()