class Phone(object):
	def __init__(self, price, type):
		self.price = price
		self.type = type
	def get_label(self):
		meg = "This is" + self.type
		return meg
	def get_information(self):
		message = "The label is "
		message += self.get_label()
		return message
price = "1000"
type = "apple"
iphone = Phone(price=price, type=type)
print(iphone.get_information())