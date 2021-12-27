# # Load pandas

# import pandas as pd

# # Webpage url                                                                                                               
# url = 'https://en.wikipedia.org/wiki/History_of_Python'

# # Extract tables
# dfs = pd.read_html(url)

# # Get first table                                                                                                           
# df = dfs[0]

# # Extract columns                                                                                                           
# df2 = df[['Version','Release date']]
# print(df2)


import pandas as pd
import matplotlib.pyplot as plt

# Webpage url                                                                                                               
url = 'http://www.climate.psu.edu/data/city_information/index.php?city=phl&page=dwa&type=big7'

# Extract tables
dfs = pd.read_html(url)

# Get first table                                                                                                           
# df2021 = dfs[2]
# df2020 = dfs[3]
df2021 = dfs[0]



df2021.to_csv('Weather2021.csv')

