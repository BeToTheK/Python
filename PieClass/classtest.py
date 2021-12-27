class Dog():
	"""docstring for ClassName"""
	def __init__(self, name,age):
		self.name = name 
		self.age = age

	def sit(self):
		print(self.name.title() + " is now sitting")

	def roll_over(self):
		print(self.name.title() + "rolled over")
		


my_dog = Dog('tink',12)
your_dog = Dog('doggo',99)

my_dog.sit()
your_dog.sit()
print(str(your_dog.age))