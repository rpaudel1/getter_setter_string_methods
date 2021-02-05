# insect_class.py
class Insects:
	# initializer method
	def __init__(self, wings, eyes, legs):
  			self.__wings = wings
  			self.__eyes = eyes
  			self. __legs = legs

    # mutator methods
	def set_wings(self, wings):
		self.__wings = wings
	def set_eyes(self, eyes):
		self.__eyes = eyes
	def set_legs(self, legs):
		self.__legs = legs

  # accessor methods
	def get_wings(self):
		return self.__wings
	def get_eyes(self):
		return self.__eyes
	def get_legs(self):
		return self.__legs
	# string method
	def __str__(self):
		return 'The wings are: ' + str(self.__wings) + ' ' \
		'The eyes are: ' + str(self.__eyes) + ' ' \
		'The legs are: ' + str(self.__legs)
