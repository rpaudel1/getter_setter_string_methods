# Importing the insect_class.py module to the main
import insect_class as ic
# create instances(object)
def main():
	fly = ic.Insects(2, 2, 6) 
	bee = ic.Insects(4, 5, 6)
	print('In house fly, ')
	print(fly)
	print('In bee, ')
	print(bee)
main()


'''
print( 'The number of wings in fly are: ', fly.get_wings())
print( 'The number of eyes in fly are: ', fly.get_eyes())
print( 'The number of legs in fly are: ',fly.get_legs())
print( 'The number of wings in bee are: ', bee.get_wings())
print( 'The number of eyes in bee are: ', bee.get_eyes())
print( 'The number of legs in bee are: ', bee.get_legs())'''	
