import pandas as pd

# df = pd.read_csv('data.csv')
# print(df)

my_string = 'Ske;Bonnet_phrygien;19/10/2004 12:11;751'

#First takes the string and splits it from the : to make a tuple
step_0 = my_string.split(';')
print(step_0)

# #Rips the second element from the tuple
# step_1 = step_0[1]
# print(step_1)

# #Splits the tuple in single elements at each ,
# step_2 = step_1.split(',')
# print(step_2)

# #loops through the names striping white space
# step_3 = [name.strip() for name in step_2]
# print(step_3)
'User', 'Name', 'Date', 'changes Category', 'Category', 'Date[dd/MM/yyyy HH:mm]', 'intr'