class Car(object):
	"""docstring for Car"""
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_read = 0

	def getdesc(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def readodo(self):
		return ("This car has "+str(self.odometer_read)+' miles on it')
	
	def updateodo(self,mileage):
		if mileage >= self.odometer_read:
			self.odometer_read = mileage
		else:
			print("increase the miles in updateodo")
	def incodo(self,miles):
		self.odometer_read += miles

mycar = Car("Honda","Accord",2000)
myoldcar = Car("Suby","Outback",2002)
myoldcar.odometer_read
print(myoldcar.getdesc())
print(myoldcar.readodo())
print(myoldcar.updateodo(25000))
print(myoldcar.readodo())
myoldcar.incodo(1000)
print(myoldcar.readodo())
print(myoldcar.updateodo(25555))
print(myoldcar.readodo())
myoldcar.incodo(100)
print(myoldcar.readodo())



		