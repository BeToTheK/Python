from pandas import DataFrame, read_csv


import matplotlib.pyplot as plt
import pandas as pd 
import matplotlib 


#Build a small data set using zip to loop over 2 lists
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
nat = ['Irish','Irish','Irish','German','Indian']
income = [32000,22000,11000,4000,0]

dset = list(zip(names,births,nat,income))
df = pd.DataFrame(dset,columns=['Names','Births','Nat','pay'])


#######################################################
######## Work Area ####################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Sorted = df.sort_values(['Births'], ascending=False)

print(df['Names','Births'].max())


# df = pd.read_csv('births.csv', names = ['Names','Births'])
# print(df)