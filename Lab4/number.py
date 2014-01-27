class Integer(object):
	def __init__(self, number, variable) :
		self.number = number
		self.variable = variable
	def display(self):
		print self.variable + str(self.number)

class NegativeInteger(Integer):
	def __init__(self, number):
		super(NegativeInteger, self).__init__(number, variable = "-")
	def display(self):
		Integer.display(self)
		print "This is an object of the NegativeInteger class"

if __name__=="__main__":
	x = Integer(85 , "+")
	x.display()
	y = NegativeInteger(67)
	y.display()


