import json  #

#Loads data into a list.
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)

#Print countries with a population below 1mil in 2010
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010' and float(pop_dict['Value'])<1000000:
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		print(country_name + ": " + str(population))

