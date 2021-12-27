import pygal
from random import randint

class Die():
	def __init__(self, num_sides=6):
		self.num_sides = num_sides

	def roll(self):
		return randint(1,self.num_sides)

die1 = Die()
die2 = Die()


results=[]
for roll_num in range(1000):
	result = die1.roll() + die2.roll()
	results.append(result)
freq=[]
max_rez = die1.num_sides + die2.num_sides
for value in range(2,max_rez+1):
	freek = results.count(value)
	freq.append(freek)

hist = pygal.Bar()

hist.title = "Results of D6 rolled 1000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('Two D6',freq)
hist.render_to_file('2D6_visual.svg')