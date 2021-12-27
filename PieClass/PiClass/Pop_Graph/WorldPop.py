import json  #
from countries import get_ccode
import pygal
from pygal.style import RotateStyle
#Loads data into a list.
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)

#countries population in 2010
cc_population = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_ccode(country_name)
		if code:
			cc_population[code] = population
		else:
			print("error- " + country_name)


#color codes for pop
cc_pop1,cc_pop2,cc_pop3 = {},{},{}
for cc, pop in cc_population.items():
	if pop < 10000000:
		cc_pop1[cc] = pop
		#pop = '{:,}'.format(pop)
	elif pop < 1000000000:
		cc_pop2[cc] = pop
		#pop = '{:,}'.format(pop)
	else:
		cc_pop3[cc] = pop 
		#pop = '{:,}'.format(pop)
wm_style = RotateStyle('#336699')
print(len(cc_pop1),len(cc_pop2),len(cc_pop3))		

wm = pygal.maps.world.World(style=wm_style)
wm.title = 'Population of Countries, grouped by size'
wm.add('0-10mil',cc_pop1)
wm.add('10-1bn',cc_pop2)
wm.add('1b+',cc_pop3)

wm.render_to_file('world_pop.svg')

